# Made By  Keep Credits If You Are Goanna Kang This Lol

# And Thanks To The Creator Of Autopic This Script Was Made from Snippets From That Script

# Usage .actressdp Im Not Responsible For Any Ban caused By This

import asyncio
import os
import random
import re
import urllib

import requests
from telethon.tl import functions

from userbot.utils import lightning_cmd

COLLECTION_STRING = [
    "pokemon-serena-wallpaper",
    "hd-pokemon-iphone-wallpapers",
    "pokemon-wallpaper-pikachu",
    "doraemon-3d-wallpaper-2018",
    "pokemon-serena-wallpaper",
    "anime-girls-wallpapers",
]


async def animepp():

    os.system("rm -rf donot.jpg")

    rnd = random.randint(0, len(COLLECTION_STRING) - 1)

    pack = COLLECTION_STRING[rnd]

    pc = requests.get("http://getwallpapers.com/collection/" + pack).text

    f = re.compile("/\w+/full.+.jpg")

    f = f.findall(pc)

    fy = "http://getwallpapers.com" + random.choice(f)

    print(fy)

    if not os.path.exists("f.ttf"):

        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf",
            "f.ttf",
        )

    urllib.request.urlretrieve(fy, "donottouch.jpg")


@borg.on(lightning_cmd(pattern="animedp ?(.*)"))
async def main(event):

    await event.edit(
        "**Starting Anime Profile Pic...\n\nDone !!! Check Your DP..by Black Lighhtning🏻**"
    )

    while True:

        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))

        os.system("rm -rf donottouch.jpg")

        await asyncio.sleep(600)  # Edit this to your required needs



from userbot import CMD_HELP

CMD_HELP.update(
    {
     "animedp": "`.animedp`\
     \n**USAGE**: Simultaneous Anime DPs"
     
    }
)