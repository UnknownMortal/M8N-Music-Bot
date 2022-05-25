import os
import sys

from git import Repo
from pyrogram.types import Message
from m8n.utils.filters import command
from pyrogram import Client, filters
from os import system, execle, environ
from git.exc import InvalidGitRepositoryError
from m8n.utils.decorators import sudo_users_only
from m8n.config import UPSTREAM_REPO, BOT_USERNAME, SUDO_USERS, BOT_NAME


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("main", origin.refs.main)
        repo.heads.main.set_tracking_branch(origin.refs.main)
        repo.heads.main.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Client.on_message(command(["check", f"update@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def check(_, message: Message):
    chat_id = message.chat.id
    msg = await message.reply("checking for updates..")
    update_avail = updater()
    if update_avail:
        await msg.edit("**Update available 🚀**\n\nNow you can update your bot with /update command with latest version.")
        system("git pull -f && pip3 install -r requirements.txt")
        execle(sys.executable, sys.executable, "main.py", environ)
        return
    await msg.edit("Bot is already in up-to-date mode with **[latest version](https://github.com/UnknownMortal/M8N-Music-Bot)**", disable_web_page_preview=True)
