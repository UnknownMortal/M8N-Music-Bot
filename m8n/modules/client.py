import aiofiles
import ffmpeg
import asyncio
import os
import shutil
import psutil
import subprocess
import requests
import aiohttp
import yt_dlp
import aiohttp
import random

from os import path
from typing import Union
from asyncio import QueueEmpty
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import ImageGrab
from typing import Callable

from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

from youtube_search import YoutubeSearch

from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    Voice,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden

from m8n.config import (
    SUDO_USERS,
    BOT_ID,
    ASSNAME,
    ASSUSERNAME,
    ASSID,
    START_IMG,
    SUPPORT,
    UPDATE,
    BOT_NAME,
    BOT_USERNAME,
)



@Client.on_callback_query(filters.regex("newcmds"))
async def newcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**[{BOT_NAME}]({https://t.me/{BOT_USERNAME}) Bot Commands 💡**

• /play (song name) or (YT link)
- plays the song in voice chat of your group 

• /song (song name) or (YT link)
- Downloads song in audio File 

• /tgm or /telegraph
- generate the link of given media

• /info 
- show all the information about a given user

• /search or /yt
- search link of the given song

• /ping
- Shows the ping message

• @botusername <query> 
- Get youtube url by inline mode

Powered by **@{UPDATE}** !!""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton(
                        "Admins", callback_data="newadmins"),
                    InlineKeyboardButton(
                        "Sudo/Owner", callback_data="newsudo")
                ],
              [InlineKeyboardButton("⬅️ Go Back", callback_data="cbhome")]]
        ),
    )


@Client.on_callback_query(filters.regex("newsudo"))
async def newsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Owner & Sudo Commands 💡**

• /broadcast (massage)
- Broadcast msg through bot

• /gcast (massage) 
- Broadcast msg with pin

• /restart 
- Restart bot from server

• /exec
- Execute any code

• /stats
- Get all statistics

• /update
- Update bot with latest version

• /gban or /ungban
- Global Ban system

• /leaveall 
- leaving assistant from all chats

Powered by **@{UPDATE}** !!""",
        reply_markup=InlineKeyboardMarkup(
            [
              
              [InlineKeyboardButton("⬅️ Go Back", callback_data="newcmds")]]
        ),
    )



@Client.on_callback_query(filters.regex("newadmins"))
async newadmins(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f"""• /skip 
- skips music in the voice Chat 

• /pause 
- Pause music in the voice chat 

• /resume 
- Resumes music in the voice Chat

• /end or /stop
- stop playing music in the group's voice chat

• /cleandb
- Clears all raw files in your group which is uploaded by bot

• /userbotjoin
- invites the music assistant of the bot in your group

• /userbotleave
- Bot's music assistant will leaves your group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 Go Back", callback_data="newcmds")
                ],
            ]
        ),
    )
