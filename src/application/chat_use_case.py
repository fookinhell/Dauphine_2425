from src.domain.chat_service import ChatService

class ChatUseCase:
    def __init__(self, chat_service: ChatService):
        self.chat_service = chat_service

    def execute(self, message: str, chat_history: list) -> str:
        return self.chat_service.chat(message, chat_history)