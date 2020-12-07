
#telegram channel @javes05
#from https://t.me/pldhsys

from userbot.javes_main.heroku_var import Var
import io
import json
import math
import os
import re
import time
from userbot import bot as borg
from userbot import CMD_HELP,  client
from userbot.javes_main.heroku_var import Config
from telethon import Button, custom, events

from userbot import CMD_LIST
from userbot import tebot as tgbot
from telethon.tl.custom import Button 
from telethon import events
from telethon import sync
import io, os
from userbot import CMD_HELP,  client
from userbot.events import javes05
from userbot import bot as borg
try:
  from userbot import tebot
except:
   tebot = None
   pass




 






IN = os.environ.get("INLINE_MODE", None)
BT = os.environ.get("BOT_TOKEN", None)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
if IN:
  @javes05(outgoing=True, pattern="^!help(?: |$|\n)([\s\S]*)")
  async def ban(event):
    if not BT:
       return await event.edit (" Error Add bot token as BOT_TOKEN in heroku var or set inline mode off ")
    mbt = await tebot.get_me()
    try:
       results = await event.client.inline_query(mbt.username, "helpme" )
    except:
       return await  event.edit (" Error go @BotFather and enable inline mode to your bot for use this mode")
    return await results[0].click( event.chat_id, reply_to=event.reply_to_msg_id, hide_via=False )
   

if tebot:

 @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret_(.*)")))
 async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/secrets.txt"):
            jsondata = json.load(open("./userbot/secrets.txt"))
            try:
                message = jsondata[f"{timestamp}"]
                userid = message["userid"]
                ids = [userid, me.id]
                if event.query.user_id in ids:
                    encrypted_tcxt = message["text"]
                    reply_pop_up_alert = encrypted_tcxt
                else:
                    reply_pop_up_alert = "why were you looking at this  go away and do your own work"
            except KeyError:
                reply_pop_up_alert = "This message no longer exists in bot server"
        else:
            reply_pop_up_alert = "This message no longer exists "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
 @tebot.on(events.CallbackQuery)
 async def handler(event):
  try:
    me = await client.get_me()
    if not event.query.user_id == me.id:
        return await event.answer("Sorry, You dont have permission to  Access me!", alert=True)
    et = event.data.decode("UTF-8")
    if et == "back":
        sad = sad2 = sad3 = sad4 = None
        lol = 0
        tbu = [[ Button.inline('❌ Close menu', b'close'), ]] 
        for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
        if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
        if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
        if sad3:
           tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
        return await event.edit ("For Support, Report bugs & help @errorsender_bot", buttons=tbu, link_preview=False)   
    if et == "close":
        return await event.edit (" Help Menu Closed")   
    if et in CMD_HELP: 
          fci = [[Button.inline('Go back', 'back'),Button.inline('❌ Close menu', b'close')]]            
          await event.edit(str(CMD_HELP[et]), buttons=fci)
    else:
    	await event.answer("Please Wait Sir", alert=True)
  except Exception as e:     
    	return await event.edit(str(e))


        
if tebot:
 @tebot.on(events.InlineQuery)  
 async def inline_handler(event):
  me = await client.get_me()  
  builder = event.builder
  query = event.text
  split = query.split(' ', 1) 
  result = None 
  hmm = re.compile("secret (.*) (.*)") 
  match = re.findall(hmm, query)
  if event.query.user_id == me.id and query.startswith("secrete"):
            markdown_note = query[7:]
            prev = 0
            note_data = ""
            buttons = []
            for match in BTN_URL_REGEX.finditer(markdown_note):
                # Check if btnurl is escaped
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                # if even, not escaped -> create button
                if n_escapes % 2 == 0:
                    # create a thruple with button label, url, and newline
                    # status
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                # if odd, escaped -> move along
                else:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            result = builder.article(
                title="secrete",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
  if event.query.user_id == me.id and match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        sandy = f"@{u.username}"
                    else:
                        sandy = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    # ValueError: Could not find the input entity
                    sandy = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    sandy = f"@{u.username}"
                else:
                    sandy = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("show message 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title="secret",
                text=f"🔒 A whisper message to {sandy}, Only he/she can open it.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))  
  if not event.query.user_id == me.id:      
      return
  if query.startswith("helpme"):
      sad = sad2 = sad3 = sad4 = None
      lol = 0
      tbu = [[ Button.inline('❌ Close menu', b'close'), ]] 
      for i in CMD_HELP:
            if lol == 0:
               sad = str(i)
               lol = 1
            elif lol == 1:
                sad2 = str(i)
                lol = 2
            elif lol == 2:
                sad3 = str(i)
                lol = 3
            elif lol == 3:
                sad4 = str(i)
                lol = 0
            if sad and sad2 and sad3 and sad4:
               tbu += [[ Button.inline(f"{sad}" , f"{sad}"), Button.inline(f"{sad2}"  , f"{sad2}"), Button.inline(f"{sad3}" , f"{sad3}"), Button.inline(f"{sad4}" , f"{sad4}")]]   
               sad = sad2 = sad3 = sad4 = None 
      if sad:
	        tbu += [[ Button.inline(f"{sad}"  , f"{sad}")]]   
      if sad2:
	        tbu += [[ Button.inline(f"{sad2}"  , f"{sad2}")]]   
      if sad3:
	       tbu += [[ Button.inline(f"{sad3}"  , f"{sad3}")]]   
      result = builder.article("Help menu", text = "For Support, Report bugs & help @errorsender_bot", buttons=tbu, link_preview=False)      
      return await event.answer([result])
  return

def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
# Darkcobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,, 
#
#
#hehehhe
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
# aur  unload load back close open kang kara ya idea bhi le to credit dena pehli 6 line nahi to bhut bura hoga tumara sath
from math import ceil
import asyncio
from userbot import CMD_HELP, BOTLOG, BOTLOG_CHATID,client
import os
from userbot.events import javes05, bot, rekcah05
from userbot.util import admin_cmd
from userbot import tebot as tgbot
from userbot import bot as borg
javes = client = bot
from telethon import events

import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io
#ABEE O KANGAR  BACK OPEN CLSE BTN KANG KIYA TO YE LONE CHIPKA DENA AUR GLOBALS K BINA NAHI CHALAGA aur global 5 gaja diff name and manipulation se imported hai 
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
from userbot.utils import remove_plugin,load_module
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,@danish_00,@ProgrammingError also v changed Pop up or inline help to text
import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST
#A stark bhai chori karna aaya ho kya friday me ek bar back btn kang kar k man nahi bhara 
#Agar stark nahi ho to kon hai be tu jo bhi hai kang karna he aaya hai mera back , open btn so get lost
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

# 🇦 🇦 🇵     🇾 🇦 🇭 🇦    🇦 🇦 🇾 🇪    🇰 🇮 🇸     🇱 🇮 🇾 🇪 ??

# 🇨 🇭 🇦 🇱 🇴      🇸 🇮 🇷    🇵 🇱 🇪 🇦 🇸 🇪    🇬 🇪 🇹 🇴 🇺 🇹    



    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            me = await client.get_me()
            if event.query.user_id == me.id :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpr")
                await event.edit("`>>>\n\nReopened The Main Menu ` ", buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)
       
  #       🇮 🇹 🇳 🇦    🇰 🇾 🇺   🇸 🇵 🇾     🇰 🇷    🇷 🇭 🇪     🇭 🇴      🇸 🇭 🇦 🇦 🇩 🇮    🇰 🇷 🇳 🇮    🇭    🇰 🇾 🇦   🇧 🇸 🇩 🇰 

    @tgbot.on(events.InlineQuery(pattern=r"helpr"))  # pylint:disable=E0602
    async def inline_id_handler(event: events.InlineQuery.Event):
        builder = event.builder
        result = None
        query = event.text
        me = await client.get_me()
        if event.query.user_id == me.id and query.startswith("helpr"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpr")
            result = builder.article(" Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "Please get your own Userbot😁😁"
              await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))#hehe
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()  # pylint:disable=E0602
        if event.query.user_id == me.id:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_LIST, "helpr")
          
            await event.edit(buttons=dc)
        else:
            Cobra = "Please get your own Userbot"
            await event.answer(Cobra)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()  # pylint:disable=E0602
        if event.query.user_id == me.id:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpr"
            )
            
            await event.edit(buttons=dc)
        else:
              TheDark = "Please get your own Userbot😁😁"
              await event.answer(TheDark)
 #hehehehehhehhehhehe   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"closer")))
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        if event.query.user_id == me.id:
            danish = custom.Button.inline("◤✞ 𝕺𝖕𝖊𝖓 𝕸𝖆𝖎𝖓 𝕸𝖊𝖓𝖚 𝕬𝖌𝖆𝖎𝖓 ✞◥", data="open")
            await event.edit("`Main Menu Has Been Closed`", buttons=danish)
        else:
            reply_pop_up_alert = "Please get your own Userbot😁😁"
            await event.answer(reply_pop_up_alert)
   

  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"bus_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        me = await client.get_me()
        if not event.query.user_id == me.id:
            atul= "Please get your own Userbot😁😁"
            await event.answer(atul)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        global shivam_sh1vam
        shivam_sh1vam="{}".format(plugin_name)
        help_string = "Commands found in {}:\n".format(plugin_name)
        k = "💠🔮💎"
        u = 0
        for i in CMD_LIST[plugin_name]:
            u += 1
            help_string += str(k[u % 3]) + " " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += "😁"

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n __Click on buttons below to load or unload them..report us if you find any bug__\n\n **©DARKCOBRA USERBOT**".format(plugin_name)
        )
        try:
            me = await client.get_me()
            if event.query.user_id == me.id :
                dc = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                await event.edit(reply_pop_up_alert, buttons=dc)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)#hehe
        except: 
            me = await client.get_me()
            if event.query.user_id == me.id :
                sh1vam = [custom.Button.inline("◤✞ 𝕲𝖔 𝕭𝖆𝖈𝖐 ✞◥",data="backr({})".format(shivam)),custom.Button.inline("◤✞ 𝕮𝖑𝖔𝖘𝖊 ✞◥", data="closer")]
                halps = "Do .hlp {} to get the list of commands.".format(plugin_name)
                await event.edit(halps,buttons=sh1vam)
            else:
                reply_pop_up_alert = "Please get your own Userbot, and don't use mine for more info visit @DARK_COBRA_SUPPORT!"
                await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"load\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              me = await client.get_me()
              if event.query.user_id == me.id :
                    
#  🇦 🇷 🇪      🇧 🇸 🇩 🇰      🇮 🇸 🇸 🇪    🇰 🇦 🇳 🇬  🇲 🇦 🇹   🇰 🇷    🇷 🇪   🇲 🇨 
                    
                    try:
                        fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                        load_module(event.data_match.group(1).decode("UTF-8"))# kyu sir kang krne m musil aa rhi h kya ... Bolo help kr du kya 😂😂😂
                        await event.edit( "`Your DarkCobra Has Successfully loaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e))+ " Successfully loaded" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝖀𝖓𝖑𝖔𝖆𝖉 ",data="unload({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot"
                    await event.answer(reply_pop_up_alert)
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"unload\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
              me = await client.get_me()
              if event.query.user_id == me.id :
                    
                    
                    try:
                        fcix = [custom.Button.inline(" 𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                        remove_plugin(event.data_match.group(1).decode("UTF-8"))#kyu sir kang krne m muskil ho rhi h kya bologe toh help krdu 😂😂
                        await event.edit( "`Successfully unloaded` >>>" + str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
                    except Exception as e:
                        await event.edit("Error{}".format(shortname, str(e)) +"Successfully unloaded"+ str(event.data_match.group(1).decode("UTF-8")),buttons=fcix)
              else:
                    shortname = event.data_match.group(1).decode("UTF-8")
                    fcix = [custom.Button.inline("  𝕭𝖆𝖈𝖐 ",data="backr({})".format(shivam)),custom.Button.inline(" 𝕮𝖑𝖔𝖘𝖊 ", data="closer"),custom.Button.inline(" 𝕷𝖔𝖆𝖉 ",data="load({})".format(shivam_sh1vam))]
                    reply_pop_up_alert = "Please get your own Userbot"
                    await event.answer(reply_pop_up_alert)#hehehe
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backr\((.+?)\)")))
   
    async def on_plug_in_callback_query_handler(event):
            
            me = await client.get_me()
            if event.query.user_id == me.id :
                try:
                    current_page_number = int(event.data_match.group(1).decode("UTF-8"))
                    buttons = paginate_help(current_page_number, CMD_HELP, "helpr")
                    await event.edit("`>>> Here Is The Main Menu `", buttons=buttons)
                except:
                    buttons = paginate_help(0, CMD_HELP, "helpr")
                    await event.edit("`>>> Here Is The Main Menu `", buttons=buttons)
            else:
                reply_pop_up_alert = "Please get your own Userbot"
                await event.answer(reply_pop_up_alert)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows =int(os.environ.get("NO_OF_COLM_TO_DESPLAY_IN_HELP",5))
    number_of_cols = int(os.environ.get("NO_OF_ROWS_TO_DESPLAY_IN_HELP",5))
    multi = os.environ.get("EMOJI_TO_DESPLAY_IN_HELP","🔥")
    mult2i = os.environ.get("EMOJI2_TO_DESPLAY_IN_HELP","💧")
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {} {}".format(random.choice(list(multi)), x,random.choice(list(mult2i))),
        data="bus_plugin_{}".format(x))
        for x in helpable_plugins]
    '''z=[]
    for i in range(0,number_of_rows+1):
        x=modules[i::number_of_cols]
        z.append(x)
    pairs =  list(zip(z))'''
    pairs =  list(zip(modules[0::number_of_cols],modules[1::number_of_cols],modules[2::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    global shivam
    modulo_page = page_number % max_num_pages
    shivam=modulo_page
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("◃:✮𝙿𝚁𝙴𝚅.❃", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⋇⋆𝙲𝙻✦𝚂𝙴⋆⋇", data="closer"),
             custom.Button.inline("❃.𝙽𝙴𝚇𝚃✮:▹", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs

# chal nikal 
# gtfo
# SED aagye aap😂




