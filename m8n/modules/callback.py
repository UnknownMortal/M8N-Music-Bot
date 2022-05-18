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
        f"""Hello 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

Check out all the commands given below by Click on the given inline buttons !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Sudo Users", callback_data=" "),
                ],[
                    InlineKeyboardButton("Everyone", callback_data=" "),
                    InlineKeyboardButton("Group Admins", callback_data=" "),
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbhome")
                ],
            ]
        ),
    ) 
