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
                        "Source code", url=f"https://github.com/UnknownMortal/M8N-Music-Bot"),
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


@Client.on_callback_query(filters.regex("cbcmnds"))
async def cbcmnds(_, query: CallbackQuery):
        await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» Check out the menu below to read the module information & see the list of available Commands !
All commands can be used with (`! / .`) handler""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👩🏻‍💼 Users Commands", callback_data="user_command"),
                ],[
                    InlineKeyboardButton("Sudo Commands", callback_data="sudo_command"),
                    InlineKeyboardButton("Owner Commands", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="home_start")
                ],
            ]
        ),
    ) 
