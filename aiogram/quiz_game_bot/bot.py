import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from questions import questions

API_TOKEN = '7752865495:AAEMFHIz50rnAeBRS_m-LMbLPynvqP-f1-o'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Состояния
class Quiz(StatesGroup):
    Qn = State()
    Score = State()

# Старт
@dp.message(F.text == "/start")
async def start_quiz(message: types.Message, state: FSMContext):
    await state.set_state(Quiz.Qn)
    await state.update_data(q_index=0, score=0)
    await send_question(message.chat.id, state)

# Функция отправки вопроса
async def send_question(chat_id, state: FSMContext):
    data = await state.get_data()
    q_index = data["q_index"]

    if q_index >= len(questions):
        await bot.send_message(chat_id, f"Викторина окончена! Правильных ответов: {data['score']} из {len(questions)}")
        await state.clear()
        return

    q = questions[q_index]
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=opt, callback_data=opt)]
            for opt in q["options"]
        ]
    )
    await bot.send_message(chat_id, q["question"], reply_markup=markup)

# Обработка ответа
@dp.callback_query()
async def handle_answer(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    q_index = data["q_index"]
    score = data["score"]
    answer = callback.data
    correct = questions[q_index]["answer"]

    if answer == correct:
        score += 1
        await callback.message.answer("✅ Правильно!")
    else:
        await callback.message.answer(f"❌ Неправильно! Правильный ответ: {correct}")

    await state.update_data(q_index=q_index + 1, score=score)
    await send_question(callback.message.chat.id, state)

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
