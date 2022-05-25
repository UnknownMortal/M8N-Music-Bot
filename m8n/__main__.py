import asyncio
import requests
from pyrogram import Client
from pytgcalls import idle
from m8n import app
from m8n import client
from m8n.database.functions import clean_restart_stage
from m8n.database.queue import get_active_chats, remove_active_chat
from m8n.tgcalls.calls import run
from m8n.config import API_ID, API_HASH, BOT_TOKEN, BG_IMG, OWNER_ID, BOT_NAME


response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted the Bot Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)
        except Exception as e:
            print("Error came while clearing db")
            pass
    await app.send_message(OWNER_ID, "**M8N Music Bot Started Successfully !!**")
   # Copyrighted Area
    await client.join_chat("M8N_SUPPORT")
    await client.join_chat("M8N_OFFICIAL")
    print("[INFO]: STARTED")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "m8n.modules"},
).start()

run()
idle()
loop.close()
