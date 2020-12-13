from telethon import Button, custom, events
from userbot import CMD_LIST
from userbot import tebot as tgbot
from userbot import tebot
from telethon.tl.custom import Button
import os
from telethon import sync
from ..utils import admin_cmd
from userbot.events import javes05
from userbot import CMD_HELP,  client
import re
TG_BOT_USER_NAME_BF_HER=os.environ.get("TG_BOT_USER_NAME_BF_HER",None)
PROFILE_PP = os.environ.get("PROFILE_PP" , None)
ALIVE_PHOTTO = PROFILE_PP
@javes05(outgoing=True, pattern="^!Shivam(?: |$|\n)([\s\S]*)")
async def gtlost(event):
    await event.delete()
    mt = await tebot.get_me()
    results = await event.client.inline_query(mt.username, "Iam On type` !javes `or` !help ` or ` .hlp `for more info" )
    return await results[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )
if TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await client.get_me()
        if query.startswith("Iam On type` !javes `or` !help ` or ` .hlp `for more info") and event.query.user_id == me.id:
            buttons = [
                (
                    Button.url("Repo", "https://github.com/Sh1vam/javes-2.0"),
                    Button.url("Deploy", "https://heroku.com/deploy?template=https://github.com/Sh1vam/javes-3.0/blob/master"),
                    Button.url("String", "https://repl.it/@Javes786/Javes-20-String-session#main.py"),
                    Button.url("Channel", "https://t.me/plugines"),
                )
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    # title="Shivam",
                    text=query,
                    buttons=buttons,
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="Sh1vam",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Javes 3.0",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)


