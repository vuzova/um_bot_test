from aiogram import BaseMiddleware
from aiogram.types import Message
import app.database.requests as rq
from app.commands import REGISTER_COMMAND
from app.constants import ACTION_REGISTER
from app.utils import get_greeting_message, get_registered_message


class RegistrationMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event: Message, data):
        if event.text == ACTION_REGISTER or event.text == f"/{REGISTER_COMMAND}":
            is_registered = await rq.get_user(event.from_user.id)
            if is_registered:
                user = await rq.get_user(event.from_user.id)
                await event.answer(get_registered_message(user))
                return

        return await handler(event, data)