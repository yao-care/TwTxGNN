"""Tests for API-based collectors with mocked HTTP responses."""

import pytest
import responses
from responses import matchers

from twtxgnn.collectors.clinicaltrials import ClinicalTrialsCollector
from twtxgnn.collectors.pubmed import PubMedCollector
from twtxgnn.collectors.ictrp import ICTRPCollector


# Sample API responses
CLINICALTRIALS_RESPONSE = {
    "studies": [
        {
            "protocolSection": {
                "identificationModule": {
                    "nctId": "NCT12345678",
                    "briefTitle": "Warfarin in Atrial Fibrillation",
                    "officialTitle": "A Study of Warfarin for AF Treatment",
                    "organization": {"fullName": "Test University"},
                },
                "statusModule": {
                    "overallStatus": "RECRUITING",
                    "startDateStruct": {"date": "2024-01-01"},
                    "completionDateStruct": {"date": "2025-12-31"},
                },
                "designModule": {
                    "phases": ["PHASE3"],
                    "enrollmentInfo": {"count": 500},
                },
                "descriptionModule": {
                    "briefSummary": "This study evaluates warfarin efficacy.",
                },
                "eligibilityModule": {
                    "eligibilityCriteria": "Adults with AF",
                },
                "outcomesModule": {
                    "primaryOutcomes": [
                        {"measure": "Stroke prevention"},
                        {"measure": "Bleeding events"},
                    ],
                },
                "contactsLocationsModule": {
                    "locations": [
                        {"country": "United States"},
                        {"country": "Taiwan"},
                    ],
                },
            }
        }
    ]
}

PUBMED_ESEARCH_RESPONSE = {
    "esearchresult": {
        "count": "1",
        "idlist": ["12345678"],
    }
}

PUBMED_EFETCH_RESPONSE = """<?xml version="1.0" encoding="UTF-8"?>
<PubmedArticleSet>
    <PubmedArticle>
        <MedlineCitation>
            <PMID>12345678</PMID>
            <Article>
                <Journal>
                    <Title>Test Journal</Title>
                    <JournalIssue>
                        <PubDate>
                            <Year>2024</Year>
                        </PubDate>
                    </JournalIssue>
                </Journal>
                <ArticleTitle>Warfarin in Atrial Fibrillation: A Review</ArticleTitle>
                <Abstract>
                    <AbstractText>This is the abstract text.</AbstractText>
                </Abstract>
                <AuthorList>
                    <Author>
                        <LastName>Smith</LastName>
                        <ForeName>John</ForeName>
                    </Author>
                </AuthorList>
                <PublicationTypeList>
                    <PublicationType>Review</PublicationType>
                </PublicationTypeList>
            </Article>
            <MeshHeadingList>
                <MeshHeading>
                    <DescriptorName>Warfarin</DescriptorName>
                </MeshHeading>
                <MeshHeading>
                    <DescriptorName>Atrial Fibrillation</DescriptorName>
                </MeshHeading>
            </MeshHeadingList>
        </MedlineCitation>
    </PubmedArticle>
</PubmedArticleSet>
"""


class TestClinicalTrialsCollector:
    """Tests for ClinicalTrialsCollector with mocked API."""

    def test_source_name(self):
        """Should have correct source name."""
        collector = ClinicalTrialsCollector()
        assert collector.source_name == "clinicaltrials"

    @responses.activate
    def test_search_success(self):
        """Should successfully search and parse trials."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            json=CLINICALTRIALS_RESPONSE,
            status=200,
        )

        collector = ClinicalTrialsCollector()
        result = collector.search("warfarin", "atrial fibrillation")

        assert result.success is True
        assert len(result.data) == 1
        trial = result.data[0]
        assert trial["id"] == "NCT12345678"
        assert trial["registry"] == "ClinicalTrials.gov"

    @responses.activate
    def test_search_parses_fields(self):
        """Should parse all trial fields correctly."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            json=CLINICALTRIALS_RESPONSE,
            status=200,
        )

        collector = ClinicalTrialsCollector()
        result = collector.search("warfarin")

        trial = result.data[0]
        assert trial["title"] == "A Study of Warfarin for AF Treatment"
        assert trial["phase"] == "PHASE3"
        assert trial["status"] == "RECRUITING"
        assert trial["enrollment"] == 500
        assert "United States" in trial["country"]
        assert "Taiwan" in trial["country"]
        assert "Stroke prevention" in trial["endpoints"]
        assert trial["sponsor"] == "Test University"

    @responses.activate
    def test_search_empty_results(self):
        """Should handle empty results."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            json={"studies": []},
            status=200,
        )

        collector = ClinicalTrialsCollector()
        result = collector.search("nonexistent_drug_xyz")

        assert result.success is True
        assert result.data == []

    @responses.activate
    def test_search_api_error(self):
        """Should handle API errors."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            json={"error": "Internal Server Error"},
            status=500,
        )

        collector = ClinicalTrialsCollector()
        result = collector.search("warfarin")

        assert result.success is False
        assert result.data == []
        assert result.error_message is not None

    @responses.activate
    def test_search_connection_error(self):
        """Should handle connection errors."""
        import requests

        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            body=requests.exceptions.ConnectionError("Connection failed"),
        )

        collector = ClinicalTrialsCollector()
        result = collector.search("warfarin")

        assert result.success is False

    @responses.activate
    def test_search_query_params(self):
        """Should send correct query parameters."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies",
            json={"studies": []},
            status=200,
        )

        collector = ClinicalTrialsCollector(max_results=100)
        collector.search("warfarin", "af")

        # Check the request was made with correct params
        assert len(responses.calls) == 1
        request_params = responses.calls[0].request.params
        assert "warfarin AND af" in request_params.get("query.term", "")
        assert request_params.get("pageSize") == "100"

    @responses.activate
    def test_get_trial_details(self):
        """Should fetch trial details by NCT ID."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies/NCT12345678",
            json={"protocolSection": {"identificationModule": {"nctId": "NCT12345678"}}},
            status=200,
        )

        collector = ClinicalTrialsCollector()
        details = collector.get_trial_details("NCT12345678")

        assert details is not None
        assert "protocolSection" in details

    @responses.activate
    def test_get_trial_details_not_found(self):
        """Should return None for non-existent trial."""
        responses.add(
            responses.GET,
            "https://clinicaltrials.gov/api/v2/studies/NCT00000000",
            status=404,
        )

        collector = ClinicalTrialsCollector()
        details = collector.get_trial_details("NCT00000000")

        assert details is None

    def test_max_results_default(self):
        """Should have default max_results."""
        collector = ClinicalTrialsCollector()
        assert collector.max_results == 50

    def test_max_results_custom(self):
        """Should accept custom max_results."""
        collector = ClinicalTrialsCollector(max_results=100)
        assert collector.max_results == 100


class TestPubMedCollector:
    """Tests for PubMedCollector with mocked API."""

    def test_source_name(self):
        """Should have correct source name."""
        collector = PubMedCollector()
        assert collector.source_name == "pubmed"

    @responses.activate
    def test_search_success(self):
        """Should successfully search and fetch articles."""
        # Mock esearch
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            json=PUBMED_ESEARCH_RESPONSE,
            status=200,
        )
        # Mock efetch
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            body=PUBMED_EFETCH_RESPONSE,
            status=200,
        )

        collector = PubMedCollector()
        result = collector.search("warfarin", "atrial fibrillation")

        assert result.success is True
        assert len(result.data["results"]) == 1
        article = result.data["results"][0]
        assert article["pmid"] == "12345678"

    @responses.activate
    def test_search_parses_fields(self):
        """Should parse all article fields correctly."""
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            json=PUBMED_ESEARCH_RESPONSE,
            status=200,
        )
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
            body=PUBMED_EFETCH_RESPONSE,
            status=200,
        )

        collector = PubMedCollector()
        result = collector.search("warfarin")

        article = result.data["results"][0]
        assert "Warfarin in Atrial Fibrillation" in article["title"]
        assert article["journal"] == "Test Journal"
        assert article["year"] == "2024"
        assert "Smith John" in article["authors"]
        assert "Review" in article["pub_types"]
        assert "Warfarin" in article["mesh_terms"]
        assert "https://pubmed.ncbi.nlm.nih.gov/12345678/" == article["url"]

    @responses.activate
    def test_search_no_results(self):
        """Should handle no results."""
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            json={"esearchresult": {"count": "0", "idlist": []}},
            status=200,
        )

        collector = PubMedCollector()
        result = collector.search("nonexistent_xyz_123")

        assert result.success is True
        assert result.data["results"] == []

    @responses.activate
    def test_search_api_error(self):
        """Should handle API errors."""
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            status=500,
        )

        collector = PubMedCollector()
        result = collector.search("warfarin")

        assert result.success is False
        assert "query" in result.data

    @responses.activate
    def test_search_with_api_key(self):
        """Should include API key in requests."""
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            json={"esearchresult": {"idlist": []}},
            status=200,
        )

        collector = PubMedCollector(api_key="test_api_key")
        collector.search("warfarin")

        assert len(responses.calls) == 1
        request_params = responses.calls[0].request.params
        assert request_params.get("api_key") == "test_api_key"

    @responses.activate
    def test_query_string_in_result(self):
        """Should include query string in result."""
        responses.add(
            responses.GET,
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
            json={"esearchresult": {"idlist": []}},
            status=200,
        )

        collector = PubMedCollector()
        result = collector.search("warfarin", "af")

        assert result.data["query"] == "warfarin AND af"

    def test_max_results_default(self):
        """Should have default max_results."""
        collector = PubMedCollector()
        assert collector.max_results == 20

    def test_parse_invalid_xml(self):
        """Should handle invalid XML."""
        collector = PubMedCollector()
        articles = collector._parse_xml("invalid xml <not closed")
        assert articles == []

    def test_parse_empty_article(self):
        """Should skip articles without MedlineCitation."""
        collector = PubMedCollector()
        xml = """<?xml version="1.0"?>
        <PubmedArticleSet>
            <PubmedArticle></PubmedArticle>
        </PubmedArticleSet>
        """
        articles = collector._parse_xml(xml)
        assert articles == []


class TestICTRPCollector:
    """Tests for ICTRPCollector."""

    def test_source_name(self):
        """Should have correct source name."""
        collector = ICTRPCollector()
        assert collector.source_name == "ictrp"

    def test_search_returns_empty(self):
        """Should return empty results (placeholder implementation)."""
        collector = ICTRPCollector()
        result = collector.search("warfarin", "atrial fibrillation")

        # ICTRP collector is a placeholder that returns empty results
        assert result.success is True
        assert result.data == []

    def test_query_in_result(self):
        """Should include query in result."""
        collector = ICTRPCollector()
        result = collector.search("warfarin", "af")

        assert result.query["drug"] == "warfarin"
        assert result.query["disease"] == "af"
