from functools import wraps

from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden
from pyrogram.types import Message

from m8n import app
from m8n.config import SUDO_USERS
from m8n.modules.admins import member_permissions


async def authorised(message):
    chatID = message.chat.id
    return 0


async def unauthorised(message: Message):
    chatID = message.chat.id
    checking = message.from_user.mention
    text = (
        f"Hey {checking} this command only for admin with permission:"
        + f"\n❌ __Delete Message Chats__"
    )
    try:
        await message.reply_text(text)
    except ChatWriteForbidden:
        await app.leave_chat(chatID)
    return 1


async def adminsOnly(permission, message):
    chatID = message.chat.id
    if not message.from_user:
        if message.sender_chat:
            return await authorised(message)
        return await unauthorised(message)
    userID = message.from_user.id
    permissions = await member_permissions(chatID, userID)
    if userID not in SUDO_USERS and permission not in permissions:
        return await unauthorised(message)
    return await authorised(message)
