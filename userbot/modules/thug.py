
from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
if not os.path.isdir("./thug/"):
    os.makedirs("./thug/")

#made by  @THE_B_LACK_HAT Some errors solved by Sh1vam

@bot.on(admin_cmd(pattern=r"thug"))
async def scan(event):
    path = "thug"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)

    os.system('pip install opencv-python--headless')
    import cv2

    os.system('wget https://datreon.000webhostapp.com/haarcascade_frontalface_default.xml')    
    
    os.system('wget https://datreon.000webhostapp.com/mask.png')

    imagePath = lol
    
    maskPath = "mask.png"
    
    cascPath = "haarcascade_frontalface_default.xml"
   
    faceCascade = cv2.CascadeClassifier(cascPath)
   
    image = cv2.imread(imagePath)
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open(imagePath)
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "thug.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
