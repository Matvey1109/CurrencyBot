from aiogram import F, types
from aiogram.filters import Command

from bot_service.bot import dp
from currency_service.currency import exchange_currency, get_all_currencies


@dp.message(Command("start"))
async def start_handler(msg: types.Message):
    await msg.answer(text="Hello, this is Currency Bot")


@dp.message(F.text.startswith("/exchange"))
async def exchange_handler(msg: types.Message):
    base_currency, target_currency, amount = msg.text.split()[1:]
    exchange_result = await exchange_currency(
        base_currency, target_currency, float(amount)
    )
    await msg.answer(text=exchange_result)


@dp.message(Command("rates"))
async def rates_handler(msg: types.Message):
    all_currencies = await get_all_currencies()
    rates = "\n".join(all_currencies)
    await msg.answer(text=rates)
