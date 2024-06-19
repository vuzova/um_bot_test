from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb
import app.database.requests as rq

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app.commands import *
from app.constants import *
from app.utils import *

router = Router()


class Register(StatesGroup):
    name = State()
    surname = State()


class EnterScores(StatesGroup):
    subject = State()
    score = State()


async def show_action_menu(message: Message):
    await message.answer(SELECT_ACTION_PROMPT, reply_markup=kb.action())


@router.message(CommandStart())
async def cmd_start(message: Message):
    is_registered = await rq.get_user(message.from_user.id)
    if is_registered:
        user = await rq.get_user(message.from_user.id)
        await message.answer(get_greeting_message(user.name, user.surname))
        await show_action_menu(message)
    else:
        await message.answer(START_MESSAGE, reply_markup=kb.main)


@router.message(Command(REGISTER_COMMAND))
@router.message(F.text == ACTION_REGISTER)
async def register(message: Message, state: FSMContext):
    await state.update_data(tg_id=message.from_user.id)
    await state.set_state(Register.name)
    await message.answer(REGISTER_NAME_PROMPT)


@router.message(Register.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await state.set_state(Register.surname)
    await message.answer(REGISTER_SURNAME_PROMPT)


@router.message(Register.surname)
async def get_surname(message: Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    user_data = await state.get_data()
    await rq.set_user(message.from_user.id, user_data["name"], user_data["surname"])
    register_success_message = get_register_success_message(user_data["name"], user_data["surname"])
    await message.answer(register_success_message)
    await state.clear()
    await show_action_menu(message)


@router.message(Command(ENTER_SCORES_COMMAND))
@router.message(F.text == ACTION_ENTER_SCORES)
async def enter_scores(message: Message):
    await message.answer(SELECT_SUBJECT_PROMPT, reply_markup=await kb.subjects())


@router.callback_query(F.data.startswith('subject_'))
async def category(callback: CallbackQuery, state: FSMContext):
    subject_id = int(callback.data.split('_')[1])
    await state.update_data(subject_id=subject_id)
    await state.set_state(EnterScores.score)
    await callback.message.answer(ENTER_SCORE_PROMPT)
    await callback.answer()

@router.message(EnterScores.score)
async def enter_score(message: Message, state: FSMContext):
    if message.text.isdigit():
        score = int(message.text)
        if score >= 0 and score <= 100:
            user_data = await state.get_data()
            anws = await rq.set_score(message.from_user.id, user_data['subject_id'], score)
            if anws:
                await message.answer(SCORE_SAVED_MESSAGE)
            else:
                await message.answer(SCORE_UPDATE_MESSAGE)
            await state.clear()
            await show_action_menu(message)
        else:
            await message.answer(INVALID_SCORE_RANGE_MESSAGE)
    else:
        await message.answer(INVALID_SCORE_MESSAGE)


@router.message(Command(SHOW_SCORES_COMMAND))
@router.message(F.text == ACTION_SHOW_SCORES)
async def show_scores(message: Message):
    scores = await rq.get_user_scores(message.from_user.id)
    for score in scores:
        sbj = await rq.get_subject(score.subject)
        await message.answer(get_score_message(sbj.name, score.score))
