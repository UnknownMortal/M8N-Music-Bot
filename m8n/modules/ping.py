# By : @Codexun
# By : Pavan Magar


import time
from datetime import datetime

import psutil
from m8n import Music_START_TIME, app
from m8n.utils.time import get_readable_time
from pyrogram import filters


async def bot_sys_stats():
    bot_uptime = int(time.time() - Music_START_TIME)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f"""
Active time: {get_readable_time((bot_uptime))}
CPU: {cpu}%
RAM: {mem}%
Disk: {disk}%
"""
    return stats


@app.on_message(filters.command("ping"))
async def ping(_, message):
    uptime = await bot_sys_stats()
    start = datetime.now()
    response = await message.reply_text("`pinging...`")
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await response.edit(
        f"**🏓 Pong !!**\n`{resp} ms`"
    )
