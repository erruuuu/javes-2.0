from telethon.tl.custom import Button 
from telethon import events
from telethon import sync
import io, os
from userbot import client
from userbot.events import javes05

try:
  from userbot import tebot
except:
   tebot = None
   pass
@javes05(outgoing=True,disable_errors=True, pattern="^!whisper ?(.*)")
async def hmm(event):
    await event.delete()
    global text,read
    tex=event.text[9:]
    text,read=tex.split(' - ')
    m = await tebot.get_me()
    reslts = await event.client.inline_query(m.username,f"{text}")
    await reslts[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )  
@tebot.on(events.InlineQuery)  
async def inlinehandler(event):
    bilder = event.builder
    tbt = [[Button.inline('Read', b'read')]]
    reslts = bilder.article(f"{text}",text = f"{text}", buttons=tbt, link_preview=False)
    await event.answer([reslts])
@tebot.on(events.CallbackQuery)
async def ihandler(event):
    evt = event.data.decode("UTF-8")
    if evt == "read":
        await event.edit(f"{read}")
