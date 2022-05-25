from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from m8n.config import BOT_USERNAME
from m8n.config import START_PIC
from m8n.config import OWNER_ID
from m8n.config import ASSUSERNAME
from m8n.config import UPDATE
from m8n.config import SUPPORT
from m8n.config import OWNER_USERNAME
from m8n.config import BOT_NAME


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Welcome [👋]({START_PIC}) [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})**

This is the {BOT_NAME}, a Bot for playing high quality and unbreakable music in your groups voice chat.

Just add me to your group and make a admin with needed admin permission to perform a right actions !!

Use the given buttons for more 📍""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "About", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmds")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds_set(_, query: CallbackQuery):
        await query.answer("commands menu")
        await query.edit_message_text(
        f"""Hello 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

Check out all the commands given below by Click on the given inline buttons !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Sudo Users", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Everyone", callback_data="cbevery"),
                    InlineKeyboardButton("Group Admins", callback_data="cbadmins"),
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbhome")
                ],
            ]
        ),
    ) 

# Commands for Everyone !!

@Client.on_callback_query(filters.regex("cbevery"))
async def all_set(_, query: CallbackQuery):
    await query.answer("Everyone menu")
    await query.edit_message_text(
    f"""• /play (song name) or (YT link)
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
- Get youtube url by inline mode""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")
                ],
            ]
        ),
    )

# Commands for SudoUsers

@Client.on_callback_query(filters.regex("cbsudo"))
async def sudo_set(_, query: CallbackQuery):
    await query.answer("sudo menu")
    await query.edit_message_text(
    f"""• /restart 
- restarts the bot in Heroku 

• /gcast 
- broadcast your message with pin in the served Chats

• /broadcast 
- broadcast your message without pin in the served chats

• /exec <code> 
- Execute any Code given by a sudo user of the bot

• /stats
- shows the Bot's system stats

• /userbotleaveall
- force the music assistant of the bot to leave all the served Chats""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")
                ],
            ]
        ),
    )

# Commands for Group Admins

@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
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
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")
                ],
            ]
        ),
    )

# Bot about & Information

@Client.on_callback_query(filters.regex("cbabout"))
async def about_set(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""Hello 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Click on the given inline buttons to know all the information about the Bot !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/{UPDATE}")
                ],[
                    InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🎸 Assistant", url=f"https://t.me/{ASSUSERNAME}")
                ],[
                    InlineKeyboardButton("🤖 Source Code", url="https://github.com/UnknownMortal/M8N-Music-Bot")
                ],[
                    InlineKeyboardButton("⬅️ Back", callback_data="cbhome")
                ],
            ]
        ),
    )
