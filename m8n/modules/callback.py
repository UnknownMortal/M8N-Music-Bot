@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})** 
This is the Montaro Super Bot, a bot for playing high quality and unbreakable music in your groups voice chat.
Just add me to your group and make a admin with needed admin permission to perform a right actions !
Use the given buttons for more 📍""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Commands", callback_data="cbcmnds"),
                    InlineKeyboardButton(
                        "About", callback_data="cbabout")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Bot in Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmnds"))
async def cbcmnds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Music Bot Commands 💡**


• /play (song name) 
- For playing music

• /pause 
- For pausing music

• /resume 
- For resuming music

• /skip 
- For skipping current song

• /search (song name) 
- For searching music

• /song or /resso 
- For download music

• /menu or /settings
- For open menu settings

• /telegraph 
- For Telegraph link of given Media

• /info
- For to know about a user""",
        reply_markup=InlineKeyboardMarkup(
            [
               [InlineKeyboardButton("🔙 Back", callback_data="cbhome")],
            ]
        ),
    )
