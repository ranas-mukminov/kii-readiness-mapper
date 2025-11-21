from typing import Protocol, List, Dict

class AIProvider(Protocol):
    def complete(self, prompt: str) -> str: ...
    def chat(self, messages: List[Dict[str, str]]) -> str: ...

class NoopAIProvider:
    def complete(self, prompt: str) -> str:
        return "AI functionality is not configured."

    def chat(self, messages: List[Dict[str, str]]) -> str:
        return "AI functionality is not configured."
