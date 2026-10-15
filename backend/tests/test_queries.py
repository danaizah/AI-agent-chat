import pytest
from chat.queries import add_message, create_conversation, get_history

pytestmark = pytest.mark.django_db


def text_block(text: str) -> list[dict]:
    return [{"type": "text", "text": text}]


def test_history_returns_messages_in_order():
    conversation = create_conversation()
    add_message(conversation, "user", text_block("hi"))
    add_message(conversation, "assistant", text_block("hello"))

    assert get_history(conversation.id) == [
        {"role": "user", "content": text_block("hi")},
        {"role": "assistant", "content": text_block("hello")},
    ]


def test_history_is_scoped_to_conversation():
    first = create_conversation()
    second = create_conversation()
    add_message(first, "user", text_block("in first"))
    add_message(second, "user", text_block("in second"))

    assert get_history(second.id) == [
        {"role": "user", "content": text_block("in second")}
    ]
