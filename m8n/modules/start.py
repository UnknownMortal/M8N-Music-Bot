import asyncio

from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, UserNotParticipant
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
from m8n.utils.filters import command

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""**Welcome [👋]({START_PIC}) {message.from_user.mention()}**

This is the {BOT_NAME}, a bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group and make a admin with needed admin permission to perform a right actions !!

Use the given buttons for more 📍""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source Code", url=f"https://github.com/UnknownMortal/M8N-Music-Bot"),
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
           ]
        ),
    )
