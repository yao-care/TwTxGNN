"""Tests for reviewer module (LLM client and Evidence Pack generator)."""

import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

from twtxgnn.reviewer.llm_client import LLMClient, get_prompt_path
from twtxgnn.reviewer.evidence_pack import EvidencePackGenerator
from twtxgnn.collectors.bundle import CandidateInfo, EvidenceBundle


class TestLLMClient:
    """Tests for LLMClient class."""

    def test_requires_api_key(self, monkeypatch):
        """Should raise error if no API key provided."""
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)

        with pytest.raises(ValueError, match="API key not found"):
            LLMClient()

    def test_uses_env_api_key(self, monkeypatch):
        """Should use OPENAI_API_KEY from environment."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key-from-env")

        client = LLMClient()
        assert client.api_key == "test-key-from-env"

    def test_uses_provided_api_key(self, monkeypatch):
        """Should prefer provided API key over environment."""
        monkeypatch.setenv("OPENAI_API_KEY", "env-key")

        client = LLMClient(api_key="provided-key")
        assert client.api_key == "provided-key"

    def test_default_model(self, monkeypatch):
        """Should use gpt-4o as default model."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        client = LLMClient()
        assert client.model == "gpt-4o"

    def test_custom_model(self, monkeypatch):
        """Should accept custom model."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        client = LLMClient(model="gpt-3.5-turbo")
        assert client.model == "gpt-3.5-turbo"

    def test_lazy_client_init(self, monkeypatch):
        """Should not create OpenAI client until needed."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        client = LLMClient()
        assert client._client is None

    def test_client_property_is_lazy(self, monkeypatch):
        """Should not create OpenAI client until accessed."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        client = LLMClient()
        # _client should be None before accessing client property
        assert client._client is None

        # Note: We can't easily test actual OpenAI client creation
        # without installing openai package in test environment

    def test_chat_with_system_prompt(self, monkeypatch):
        """Should include system prompt in messages."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        mock_openai_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Response"))]
        mock_openai_client.chat.completions.create.return_value = mock_response

        client = LLMClient()
        client._client = mock_openai_client

        client.chat("User message", system_prompt="System prompt")

        call_args = mock_openai_client.chat.completions.create.call_args
        messages = call_args.kwargs["messages"]
        assert messages[0]["role"] == "system"
        assert messages[0]["content"] == "System prompt"
        assert messages[1]["role"] == "user"

    def test_chat_parameters(self, monkeypatch):
        """Should pass temperature and max_tokens."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        mock_openai_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Response"))]
        mock_openai_client.chat.completions.create.return_value = mock_response

        client = LLMClient()
        client._client = mock_openai_client

        client.chat("Hi", temperature=0.5, max_tokens=100)

        call_args = mock_openai_client.chat.completions.create.call_args
        assert call_args.kwargs["temperature"] == 0.5
        assert call_args.kwargs["max_tokens"] == 100

    def test_chat_with_prompt_file(self, monkeypatch, tmp_path):
        """Should read system prompt from file."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        mock_openai_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Response"))]
        mock_openai_client.chat.completions.create.return_value = mock_response

        # Create prompt file
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("You are a helpful assistant.")

        client = LLMClient()
        client._client = mock_openai_client

        client.chat_with_prompt_file("Hello", prompt_file)

        call_args = mock_openai_client.chat.completions.create.call_args
        messages = call_args.kwargs["messages"]
        assert messages[0]["content"] == "You are a helpful assistant."

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
