from abc import ABC, abstractmethod

class ChatService(ABC):
    @abstractmethod
    def chat(self, message: str, chat_history: list) -> str:
        pass