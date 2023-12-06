from aiogram import Bot, Dispatcher, types, executor
from config import token 
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

number = random.randint(1,3)
@dp.message_handler(commands='start')
async def play(message:types.Message):
    await message.answer("Я загадал число от 1 до 3 угадайте")

@dp.message_handler()
async def randomnum(message:types.Message):
    if int(message.text) == number:
        await message.answer_photo('https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg')
    else:
        await message.answer_photo('https://media.makeameme.org/created/sorry-you-lose.jpg')

executor.start_polling(dp)