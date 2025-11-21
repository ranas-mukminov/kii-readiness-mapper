from kii_readiness_mapper.ai.base import NoopAIProvider
from kii_readiness_mapper.ai.infra_text_parser import InfraTextParser
from kii_readiness_mapper.ai.narrative_reporter import NarrativeReporter

def test_ai_stubs():
    provider = NoopAIProvider()
    assert provider.complete("test") == "AI functionality is not configured."
    
    parser = InfraTextParser(provider)
    profile = parser.parse("some text")
    assert profile.name == "Parsed Organization"
    
    reporter = NarrativeReporter(provider)
    report = reporter.generate_report(None, None)
    assert "AI generation not implemented" in report
