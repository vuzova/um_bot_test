from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.constants import (ACTION_REGISTER,
                           ACTION_ENTER_SCORES,
                           ACTION_SHOW_SCORES)

from app.database.requests import get_subjects

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=ACTION_REGISTER)]
    ],
    resize_keyboard=True,
)


def action():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=ACTION_ENTER_SCORES)],
            [KeyboardButton(text=ACTION_SHOW_SCORES)]
        ],
        resize_keyboard=True,
    )


async def subjects():
    all_subjects = await get_subjects()
    kb = InlineKeyboardBuilder()
    for sbj in all_subjects:
        kb.add(InlineKeyboardButton(text=sbj.name, callback_data=f'subject_{sbj.id}'))
    return kb.adjust(3).as_markup()
