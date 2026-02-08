"""Tests for writer module (Notes Writers)."""

import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch

from twtxgnn.writer.base import BaseNotesWriter
from twtxgnn.writer.pharmacist import PharmacistNotesWriter
from twtxgnn.writer.sponsor import SponsorNotesWriter
from twtxgnn.reviewer.llm_client import LLMClient


class ConcreteNotesWriter(BaseNotesWriter):
    """Concrete implementation for testing base class."""

    writer_type = "test"
    prompt_name = "test"

    def __init__(self, llm_client=None, prompt_path=None):
        super().__init__(llm_client=llm_client)
        self._prompt_path = prompt_path or Path("/tmp/test_prompt.md")

    @property
    def prompt_path(self) -> Path:
        return self._prompt_path


class TestBaseNotesWriter:
    """Tests for BaseNotesWriter abstract class."""

    @pytest.fixture
    def mock_llm_client(self):
        """Create a mock LLM client."""
        client = Mock(spec=LLMClient)
        client.chat_with_prompt_file.return_value = "# Generated Notes\n\nContent here."
        return client

    @pytest.fixture
    def sample_evidence_pack(self):
        """Sample evidence pack for testing."""
        return {
            "candidate": {"inn": "warfarin", "indication_raw": "af"},
            "evidence": {"level": "L2"},
            "safety": {"ddi": []},
        }

    def test_cannot_instantiate_base(self, monkeypatch):
        """Should not be able to instantiate BaseNotesWriter directly."""
        monkeypatch.setenv("OPENAI_API_KEY", "test-key")

        with pytest.raises(TypeError):
            BaseNotesWriter()

    def test_generate_with_dict(self, mock_llm_client, sample_evidence_pack, tmp_path):
        """Should generate notes from dict."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate(sample_evidence_pack)

        assert "Generated Notes" in result
        mock_llm_client.chat_with_prompt_file.assert_called_once()

    def test_generate_with_json_file(
        self, mock_llm_client, sample_evidence_pack, tmp_path
    ):
        """Should load evidence pack from JSON file."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        # Create evidence pack file
        evidence_file = tmp_path / "evidence.json"
        with open(evidence_file, "w") as f:
            json.dump(sample_evidence_pack, f)

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate(evidence_file)

        assert result is not None
        mock_llm_client.chat_with_prompt_file.assert_called_once()

    def test_generate_with_md_file(self, mock_llm_client, tmp_path):
        """Should load evidence pack from Markdown file."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        # Create evidence pack markdown file
        evidence_file = tmp_path / "evidence.md"
        evidence_file.write_text("# Evidence Pack\n\nContent here.")

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate(evidence_file)

        assert result is not None

    def test_generate_with_json_string(self, mock_llm_client, tmp_path):
        """Should handle JSON string input."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        json_str = '{"candidate": {"inn": "warfarin"}}'

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate(json_str)

        # Should treat as string if file doesn't exist
        assert result is not None

    def test_clean_response_markdown_block(self, mock_llm_client, tmp_path):
        """Should remove markdown code block wrappers."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        mock_llm_client.chat_with_prompt_file.return_value = (
            "```markdown\n# Title\nContent\n```"
        )

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate({"test": "data"})

        assert not result.startswith("```")
        assert not result.endswith("```")
        assert "# Title" in result

    def test_clean_response_md_block(self, mock_llm_client, tmp_path):
        """Should remove ```md code block wrappers."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        mock_llm_client.chat_with_prompt_file.return_value = "```md\n# Title\n```"

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate({"test": "data"})

        assert not result.startswith("```")

    def test_clean_response_generic_block(self, mock_llm_client, tmp_path):
        """Should remove generic code block wrappers."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        mock_llm_client.chat_with_prompt_file.return_value = "```\n# Title\n```"

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result = writer.generate({"test": "data"})

        assert not result.startswith("```")

    def test_generate_and_save(self, mock_llm_client, tmp_path):
        """Should save generated notes to file."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        output_file = tmp_path / "output" / "notes.md"

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        result_path = writer.generate_and_save({"test": "data"}, output_file)

        assert result_path.exists()
        content = result_path.read_text()
        assert "Generated Notes" in content

    def test_generate_and_save_creates_directory(self, mock_llm_client, tmp_path):
        """Should create output directory if not exists."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        output_file = tmp_path / "nested" / "dir" / "notes.md"

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        writer.generate_and_save({"test": "data"}, output_file)

        assert output_file.exists()

    def test_temperature_passed_to_llm(self, mock_llm_client, tmp_path):
        """Should pass temperature to LLM client."""
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("Test prompt")

        writer = ConcreteNotesWriter(
            llm_client=mock_llm_client, prompt_path=prompt_file
        )
        writer.generate({"test": "data"}, temperature=0.2)

        call_args = mock_llm_client.chat_with_prompt_file.call_args
        assert call_args.kwargs["temperature"] == 0.2


class TestPharmacistNotesWriter:
    """Tests for PharmacistNotesWriter class."""

    @pytest.fixture
    def mock_llm_client(self):
        """Create a mock LLM client."""
        client = Mock(spec=LLMClient)
        client.chat_with_prompt_file.return_value = "# Pharmacist Notes\n\nContent."
        return client

    def test_writer_type(self, mock_llm_client):
        """Should have correct writer type."""
        writer = PharmacistNotesWriter(llm_client=mock_llm_client)
        assert writer.writer_type == "pharmacist"

    def test_prompt_name(self, mock_llm_client):
        """Should have correct prompt name."""
        writer = PharmacistNotesWriter(llm_client=mock_llm_client)
        assert writer.prompt_name == "pharmacist"

    def test_prompt_path(self, mock_llm_client):
        """Should return pharmacist prompt path."""
        writer = PharmacistNotesWriter(llm_client=mock_llm_client)
        path = writer.prompt_path
        assert "pharmacist" in path.name
        assert path.suffix == ".md"

    def test_generate(self, mock_llm_client):
        """Should generate pharmacist notes."""
        writer = PharmacistNotesWriter(llm_client=mock_llm_client)
        result = writer.generate({"candidate": {"inn": "warfarin"}})

        assert "Pharmacist Notes" in result
        mock_llm_client.chat_with_prompt_file.assert_called_once()


class TestSponsorNotesWriter:
    """Tests for SponsorNotesWriter class."""

    @pytest.fixture
    def mock_llm_client(self):
        """Create a mock LLM client."""
        client = Mock(spec=LLMClient)
        client.chat_with_prompt_file.return_value = "# Sponsor Notes\n\nContent."
        return client

    def test_writer_type(self, mock_llm_client):
        """Should have correct writer type."""
        writer = SponsorNotesWriter(llm_client=mock_llm_client)
        assert writer.writer_type == "sponsor"

    def test_prompt_name(self, mock_llm_client):
        """Should have correct prompt name."""
        writer = SponsorNotesWriter(llm_client=mock_llm_client)
        assert writer.prompt_name == "sponsor"

    def test_prompt_path(self, mock_llm_client):
        """Should return sponsor prompt path."""
        writer = SponsorNotesWriter(llm_client=mock_llm_client)
        path = writer.prompt_path
        assert "sponsor" in path.name
        assert path.suffix == ".md"

    def test_generate(self, mock_llm_client):
        """Should generate sponsor notes."""
        writer = SponsorNotesWriter(llm_client=mock_llm_client)
        result = writer.generate({"candidate": {"inn": "warfarin"}})

        assert "Sponsor Notes" in result
        mock_llm_client.chat_with_prompt_file.assert_called_once()


class TestWriterIntegration:
    """Integration tests for writers."""

    @pytest.fixture
    def mock_llm_client(self):
        """Create a mock LLM client."""
        client = Mock(spec=LLMClient)
        return client

    def test_pharmacist_and_sponsor_different_prompts(self, mock_llm_client):
        """Pharmacist and sponsor should use different prompts."""
        pharmacist = PharmacistNotesWriter(llm_client=mock_llm_client)
        sponsor = SponsorNotesWriter(llm_client=mock_llm_client)

        assert pharmacist.prompt_path != sponsor.prompt_path
        assert pharmacist.writer_type != sponsor.writer_type

    def test_all_writers_inherit_base(self, mock_llm_client):
        """All writers should inherit from BaseNotesWriter."""
        pharmacist = PharmacistNotesWriter(llm_client=mock_llm_client)
        sponsor = SponsorNotesWriter(llm_client=mock_llm_client)

        assert isinstance(pharmacist, BaseNotesWriter)
        assert isinstance(sponsor, BaseNotesWriter)
