"""Tests for reviewer module (LLM client and Evidence Pack generator)."""

import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from twtxgnn.reviewer.llm_client import LLMClient, get_prompt_path
from twtxgnn.reviewer.evidence_pack import EvidencePackGenerator
from twtxgnn.collectors.bundle import CandidateInfo, EvidenceBundle


class TestLLMClient:
    """Tests for LLMClient（2026-10 起改用 claude CLI，不再用 OpenAI API）."""

    RUN = "twtxgnn.reviewer.llm_client.subprocess.run"

    @staticmethod
    def _ok(stdout="Response"):
        return Mock(returncode=0, stdout=stdout, stderr="")

    def test_no_api_key_needed(self, monkeypatch):
        """Should not require any API key."""
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        client = LLMClient()
        assert client.model is None

    def test_api_key_ignored(self):
        """api_key is kept for backward compatibility and ignored."""
        client = LLMClient(api_key="ignored")
        assert not hasattr(client, "api_key")

    def test_custom_model(self):
        """Should pass --model to the CLI."""
        with patch(self.RUN, return_value=self._ok()) as run:
            LLMClient(model="sonnet").chat("Hi")
        cmd = run.call_args.args[0]
        assert cmd[:2] == ["claude", "-p"]
        assert cmd[cmd.index("--model") + 1] == "sonnet"

    def test_default_model_not_passed(self):
        """Should not pass --model when none is given."""
        with patch(self.RUN, return_value=self._ok()) as run:
            LLMClient().chat("Hi")
        assert "--model" not in run.call_args.args[0]

    def test_chat_with_system_prompt(self):
        """Should pass the system prompt as --system-prompt and the message via stdin."""
        with patch(self.RUN, return_value=self._ok()) as run:
            out = LLMClient().chat("User message", system_prompt="System prompt")
        cmd = run.call_args.args[0]
        assert cmd[cmd.index("--system-prompt") + 1] == "System prompt"
        assert run.call_args.kwargs["input"] == "User message"
        assert out == "Response"

    def test_cli_runs_without_tools_or_settings(self):
        """Should disable tools, MCP servers, slash commands and setting sources."""
        with patch(self.RUN, return_value=self._ok()) as run:
            LLMClient().chat("Hi")
        cmd = run.call_args.args[0]
        assert cmd[cmd.index("--tools") + 1] == ""
        assert "--strict-mcp-config" in cmd
        assert "--disable-slash-commands" in cmd
        assert cmd[cmd.index("--setting-sources") + 1] == ""

    def test_non_transient_error_raises(self):
        """Should raise on a non-transient CLI failure without retrying."""
        with patch(self.RUN, return_value=Mock(returncode=1, stdout="", stderr="bad flag")) as run:
            with pytest.raises(RuntimeError, match="claude CLI failed"):
                LLMClient().chat("Hi")
        assert run.call_count == 1

    def test_chat_with_prompt_file(self, tmp_path):
        """Should read system prompt from file."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("You are a helpful assistant.")
        with patch(self.RUN, return_value=self._ok()) as run:
            LLMClient().chat_with_prompt_file("Hello", prompt_file)
        cmd = run.call_args.args[0]
        assert cmd[cmd.index("--system-prompt") + 1] == "You are a helpful assistant."

    def test_chat_with_missing_prompt_file(self, monkeypatch, tmp_path):
        """Should raise error for missing prompt file."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        client = LLMClient()

        with pytest.raises(FileNotFoundError):
            client.chat_with_prompt_file("Hello", tmp_path / "nonexistent.md")


class TestGetPromptPath:
    """Tests for get_prompt_path function."""

    def test_evidence_pack_reviewer(self):
        """Should return path to evidence pack reviewer prompt."""
        path = get_prompt_path("evidence_pack_reviewer")
        assert path.name == "v1.md"
        assert "Evidence Pack Reviewer" in str(path)

    def test_pharmacist(self):
        """Should return path to pharmacist prompt."""
        path = get_prompt_path("pharmacist")
        assert path.name == "pharmacist_v1.md"
        assert "Notes Writer" in str(path)

    def test_sponsor(self):
        """Should return path to sponsor prompt."""
        path = get_prompt_path("sponsor")
        assert path.name == "sponsor_v1.md"
        assert "Notes Writer" in str(path)

    def test_invalid_prompt_name(self):
        """Should raise error for invalid prompt name."""
        with pytest.raises(ValueError, match="Unknown prompt"):
            get_prompt_path("invalid_prompt")


class TestEvidencePackGenerator:
    """Tests for EvidencePackGenerator class."""

    @pytest.fixture
    def mock_llm_client(self):
        """Create a mock LLM client."""
        client = Mock(spec=LLMClient)
        return client

    @pytest.fixture
    def sample_bundle(self):
        """Create a sample evidence bundle."""
        candidate = CandidateInfo(
            inn="warfarin",
            drugbank_id="DB00682",
            indication_raw="atrial fibrillation",
        )
        return EvidenceBundle(
            candidate=candidate,
            tfda={"found": True, "records": []},
        )

    def test_init_with_client(self, mock_llm_client):
        """Should accept existing LLM client."""
        generator = EvidencePackGenerator(llm_client=mock_llm_client)
        assert generator.llm_client == mock_llm_client

    def test_init_creates_client(self, monkeypatch):
        """Should create LLM client if not provided."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        generator = EvidencePackGenerator()
        assert generator.llm_client is not None

    def test_generate_calls_llm(self, mock_llm_client, sample_bundle):
        """Should call LLM with bundle data."""
        mock_llm_client.chat_with_prompt_file.return_value = '```json\n{"test": "data"}\n```\n\n# Summary'

        generator = EvidencePackGenerator(llm_client=mock_llm_client)
        generator.generate(sample_bundle)

        mock_llm_client.chat_with_prompt_file.assert_called_once()
        call_args = mock_llm_client.chat_with_prompt_file.call_args
        assert "warfarin" in call_args.kwargs["user_message"]

    def test_parse_response_json(self, mock_llm_client):
        """Should extract JSON from response."""
        generator = EvidencePackGenerator(llm_client=mock_llm_client)

        response = '''```json
{"candidate": {"inn": "warfarin"}, "evidence_level": "L2"}
```

# Summary
This is the summary.'''

        json_data, md_data = generator._parse_response(response)

        assert json_data["candidate"]["inn"] == "warfarin"
        assert json_data["evidence_level"] == "L2"

    def test_parse_response_markdown(self, mock_llm_client):
        """Should extract Markdown from response."""
        generator = EvidencePackGenerator(llm_client=mock_llm_client)

        response = '''```json
{"test": "data"}
```

```markdown
# Evidence Pack Summary

## Candidate Snapshot
- Drug: Warfarin
```'''

        json_data, md_data = generator._parse_response(response)

        assert "Candidate Snapshot" in md_data
        assert "Warfarin" in md_data

    def test_parse_response_fallback(self, mock_llm_client):
        """Should handle responses without markdown blocks."""
        generator = EvidencePackGenerator(llm_client=mock_llm_client)

        response = '''```json
{"test": "data"}
```

# Evidence Level
L2'''

        json_data, md_data = generator._parse_response(response)

        assert json_data == {"test": "data"}
        assert "Evidence Level" in md_data or "L2" in md_data

    def test_parse_response_invalid_json(self, mock_llm_client):
        """Should handle invalid JSON gracefully."""
        generator = EvidencePackGenerator(llm_client=mock_llm_client)

        response = '''```json
{invalid json}
```

# Summary'''

        json_data, md_data = generator._parse_response(response)

        assert json_data == {}

    def test_generate_and_save(self, mock_llm_client, sample_bundle, tmp_path):
        """Should save generated files."""
        mock_llm_client.chat_with_prompt_file.return_value = '''```json
{"candidate": {"inn": "warfarin"}}
```

# Summary
Test summary content.'''

        generator = EvidencePackGenerator(llm_client=mock_llm_client)
        json_path, md_path = generator.generate_and_save(sample_bundle, tmp_path)

        assert json_path.exists()
        assert md_path.exists()
        assert "warfarin" in json_path.name
        assert "atrial_fibrillation" in json_path.name

        # Verify content
        with open(json_path) as f:
            data = json.load(f)
            assert data["candidate"]["inn"] == "warfarin"

    def test_generate_and_save_creates_directory(
        self, mock_llm_client, sample_bundle, tmp_path
    ):
        """Should create output directory if not exists."""
        mock_llm_client.chat_with_prompt_file.return_value = '```json\n{}\n```'

        generator = EvidencePackGenerator(llm_client=mock_llm_client)
        output_dir = tmp_path / "nested" / "dir"
        generator.generate_and_save(sample_bundle, output_dir)

        assert output_dir.exists()

    def test_generate_temperature(self, mock_llm_client, sample_bundle):
        """Should pass temperature to LLM."""
        mock_llm_client.chat_with_prompt_file.return_value = '```json\n{}\n```'

        generator = EvidencePackGenerator(llm_client=mock_llm_client)
        generator.generate(sample_bundle, temperature=0.1)

        call_args = mock_llm_client.chat_with_prompt_file.call_args
        assert call_args.kwargs["temperature"] == 0.1
