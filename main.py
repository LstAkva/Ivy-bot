from typing import Any
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from aiogram.handlers import MessageHandler
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
import logging
import sys

dp = Dispatcher()
# Replace with your bot token
TOKEN = '8124872653:AAEDEZb0x4yBkDDSsGofyzksZDU2uZjuJpI'

# Create the bot and dispatcher
my_router = Router()

# Set the bot owner's ID (replace with your ID)
OWNER_ID = 1024157594

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!\nWrite a message and I'll deliver it!")

@dp.message()
async def message_handler(message: Message) -> Any:
    await message.forward(OWNER_ID)
    await message.answer(f'Message delivered! Any questions left?')
@dp.edited_message()
async def edited_message_handler(edited_message: Message) -> Any:
    await edited_message.forward(OWNER_ID)

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())