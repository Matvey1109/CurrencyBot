import asyncio
import logging

from bot_service.bot import dp, tg_bot
from bot_service.handlers import *
from currency_service.currency import update_currency_rates


async def schedule():
    while True:
        await asyncio.sleep(24 * 60 * 60)  # Wait for 24 hours
        await update_currency_rates()


async def main():
    logging.basicConfig(level=logging.INFO)
    await update_currency_rates()

    loop = asyncio.get_event_loop()
    loop.create_task(schedule())
    await dp.start_polling(tg_bot)


if __name__ == "__main__":
    asyncio.run(main())
