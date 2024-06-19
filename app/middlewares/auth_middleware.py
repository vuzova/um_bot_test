from aiogram import BaseMiddleware
from aiogram.types import Message
import app.database.requests as rq
from app.commands import SHOW_SCORES_COMMAND, ENTER_SCORES_COMMAND
from app.constants import ACTION_ENTER_SCORES, ACTION_SHOW_SCORES, INVALID_USER_MESSAGE


class AuthMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event: Message, data):
        if event.text in (ACTION_ENTER_SCORES, ACTION_SHOW_SCORES) or \
                event.text in(f"/{ENTER_SCORES_COMMAND}", f"/{SHOW_SCORES_COMMAND}"):
            is_registered = await rq.get_user(event.from_user.id)
            if not is_registered:
                await event.answer(INVALID_USER_MESSAGE)
                return

        return await handler(event, data)
