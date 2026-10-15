from chat.models import Conversation, Message


def create_conversation(title: str = "") -> Conversation:
    return Conversation.objects.create(title=title)


def add_message(conversation: Conversation, role: str, content: list[dict]) -> Message:
    return Message.objects.create(conversation=conversation, role=role, content=content)


def get_history(conversation_id: int) -> list[dict]:
    messages = Message.objects.filter(conversation_id=conversation_id)
    return [{"role": m.role, "content": m.content} for m in messages]
