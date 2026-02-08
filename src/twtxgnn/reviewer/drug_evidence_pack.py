"""Drug-centric Evidence Pack generator using LLM."""

import json
import re
from pathlib import Path

from ..collectors.drug_bundle import DrugBundle
from .llm_client import LLMClient


class DrugEvidencePackGenerator:
    """Generates Drug Evidence Pack from a DrugBundle using LLM.

    Uses the Evidence Pack Reviewer v2 (drug-centric) prompt to process
    the bundle and output structured drug_evidence_pack.json and drug_evidence_pack.md.
    """

    def __init__(
        self,
        llm_client: LLMClient | None = None,
        model: str = "gpt-4o",
    ):
        """Initialize the generator.

        Args:
            llm_client: Optional LLMClient instance. If not provided, creates one.
            model: Model to use if creating a new LLMClient.
        """
        self.llm_client = llm_client or LLMClient(model=model)
        self.prompt_path = self._get_prompt_path()

    def _get_prompt_path(self) -> Path:
        """Get the path to the drug-centric prompt (v3)."""
        from ..paths import get_project_root
        return get_project_root() / "prompts" / "Evidence Pack Reviewer" / "v3_drug_centric.md"

    def generate(
        self,
        bundle: DrugBundle,
        temperature: float = 0.3,
    ) -> tuple[dict, str]:
        """Generate Drug Evidence Pack from a bundle.

        Args:
            bundle: The DrugBundle containing collected data
            temperature: LLM temperature (lower = more deterministic)

        Returns:
            Tuple of (drug_evidence_pack_json, drug_evidence_pack_md)
        """
        # Prepare the user message with the bundle data
        user_message = f"""請處理以下藥物為中心的資料，產生 Drug Evidence Pack：

```json
{bundle.to_json()}
```

這個藥物有 {len(bundle.drug.predicted_indications)} 個預測的新適應症。
請針對每個預測適應症進行分析，並輸出：
1. drug_evidence_pack.json（完整 JSON 結構）
2. drug_evidence_pack.md（摘要文件）
"""

        # Call the LLM
        response = self.llm_client.chat_with_prompt_file(
            user_message=user_message,
            prompt_file=self.prompt_path,
            temperature=temperature,
        )

        # Parse the response (store for debug if needed)
        self._last_response = response
        return self._parse_response(response)

    def _parse_response(self, response: str, debug_path: Path | None = None) -> tuple[dict, str]:
        """Parse LLM response to extract JSON and Markdown.

        Args:
            response: Raw LLM response text
            debug_path: Optional path to save raw response for debugging

        Returns:
            Tuple of (drug_evidence_pack_json, drug_evidence_pack_md)
        """
        # Save raw response for debugging
        if debug_path:
            debug_path.mkdir(parents=True, exist_ok=True)
            raw_path = debug_path / "raw_llm_response.txt"
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(response)
            print(f"  - Raw response saved: {raw_path}")

        evidence_json = {}
        evidence_md = ""

        # Try to extract JSON from code blocks using a two-step approach
        json_candidates = []

        # Pattern 1: Find ```json ... ``` blocks (case insensitive)
        json_block_pattern = r"```[jJ][sS][oO][nN]\s*([\s\S]*?)```"
        json_candidates.extend(re.findall(json_block_pattern, response))

        # Pattern 2: Find generic code blocks with JSON-like content
        if not json_candidates:
            generic_block_pattern = r"```\s*(\{[\s\S]*?\})\s*```"
            json_candidates.extend(re.findall(generic_block_pattern, response))

        # Try to parse each candidate, prefer the largest valid JSON
        valid_jsons = []
        for candidate in json_candidates:
            candidate = candidate.strip()
            if not candidate:
                continue
            try:
                parsed = json.loads(candidate)
                if isinstance(parsed, dict):
                    valid_jsons.append((len(candidate), parsed))
            except json.JSONDecodeError:
                # Try to fix common issues (trailing commas)
                try:
                    fixed = re.sub(r',([\s]*[}\]])', r'\1', candidate)
                    parsed = json.loads(fixed)
                    if isinstance(parsed, dict):
                        valid_jsons.append((len(fixed), parsed))
                except json.JSONDecodeError:
                    continue

        # If we have valid JSONs, pick the largest one (most complete)
        if valid_jsons:
            valid_jsons.sort(key=lambda x: x[0], reverse=True)
            evidence_json = valid_jsons[0][1]
        else:
            # Fallback: Try to find JSON object without code blocks
            fallback_patterns = [
                r'(\{"meta"\s*:\s*\{[\s\S]*)',
                r'(\{"drug"\s*:\s*\{[\s\S]*)',
            ]
            for pattern in fallback_patterns:
                match = re.search(pattern, response)
                if match:
                    json_text = match.group(1)
                    parsed = self._try_parse_json_with_brace_matching(json_text)
                    if parsed:
                        evidence_json = parsed
                        print("  - Note: Found JSON without code blocks using fallback")
                        break

            if not evidence_json:
                print("  - Warning: No valid JSON found in LLM response")
                print(f"  - Response length: {len(response)} chars")
                if json_candidates:
                    print(f"  - Found {len(json_candidates)} JSON candidate(s) but all failed to parse")

        # Try to extract Markdown section (case insensitive)
        md_pattern = r"```[mM][aA][rR][kK][dD][oO][wW][nN]\s*([\s\S]*?)```"
        md_matches = re.findall(md_pattern, response)

        if md_matches:
            # Pick the largest markdown block
            evidence_md = max(md_matches, key=len).strip()
        else:
            # If no markdown block, try to find content after the JSON
            parts = response.split("```")
            if len(parts) >= 3:
                for i in range(len(parts) - 1, -1, -1):
                    part = parts[i].strip()
                    if part and not part.startswith("{") and not part.lower().startswith("json"):
                        if "藥物基本資訊" in part or "預測新適應症" in part or "老藥新用" in part:
                            evidence_md = part
                            break

        # If still no markdown, use the whole response minus JSON blocks
        if not evidence_md:
            temp = response
            # Remove all code blocks
            temp = re.sub(r"```[\s\S]*?```", "", temp)
            evidence_md = temp.strip()

        return evidence_json, evidence_md

    def _try_parse_json_with_brace_matching(self, text: str) -> dict | None:
        """Try to parse JSON by finding matching braces.

        Args:
            text: Text starting with a JSON object

        Returns:
            Parsed JSON dict or None if parsing fails
        """
        if not text or not text.startswith("{"):
            return None

        # Count braces to find the end of the JSON object
        depth = 0
        in_string = False
        escape_next = False
        end_pos = -1

        for i, char in enumerate(text):
            if escape_next:
                escape_next = False
                continue

            if char == "\\":
                escape_next = True
                continue

            if char == chr(34) and not escape_next:
                in_string = not in_string
                continue

            if in_string:
                continue

            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end_pos = i + 1
                    break

        if end_pos > 0:
            json_text = text[:end_pos]
            try:
                return json.loads(json_text)
            except json.JSONDecodeError:
                # Try to fix common issues
                try:
                    fixed = re.sub(r",(\s*[}\]])", r"\1", json_text)
                    return json.loads(fixed)
                except json.JSONDecodeError:
                    pass

        return None

    def generate_and_save(
        self,
        bundle: DrugBundle,
        output_dir: str | Path,
        temperature: float = 0.3,
    ) -> tuple[Path, Path]:
        """Generate Drug Evidence Pack and save to files.

        Args:
            bundle: The DrugBundle containing collected data
            output_dir: Directory to save output files
            temperature: LLM temperature

        Returns:
            Tuple of (json_path, md_path)
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        evidence_json, evidence_md = self.generate(bundle, temperature)

        # Save raw response for debugging
        if hasattr(self, '_last_response') and self._last_response:
            raw_path = output_dir / "raw_llm_response.txt"
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(self._last_response)
            print(f"  - Raw response saved: {raw_path}")

        # Generate filename from drug name
        drug_slug = bundle.drug.inn.lower().replace(" ", "_")

        base_name = f"{drug_slug}_drug_evidence_pack"

        # Save JSON
        json_path = output_dir / f"{base_name}.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(evidence_json, f, indent=2, ensure_ascii=False)

        # Save Markdown
        md_path = output_dir / f"{base_name}.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(evidence_md)

        return json_path, md_path
