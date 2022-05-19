import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم اعاده تشغيل موسيقى زوين**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["انطيني الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 اهلا {m.from_user.mention}!

𝘰𝘳𝘥𝘦𝘳𝘴 𝘮𝘶𝘴𝘪𝘤 𝘵𝘦𝘭𝘦𝘵𝘩𝘰𝘯
——————×—————

⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}شغل  + اسم الاغنية` ]
⧉ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}شغل فيديو  + اسم الاغنية` ]
———————×———————

⧉ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `{HNDLR}ايقاف مؤقت` ] 
⧉ | لأعاده تشغيل الاغنية ⇦  [ `{HNDLR}تشغيل المؤقت` ]
⧉ | لأيقاف الاغنية  ⇦ [ `{HNDLR}كافي` ] 
———————×———————

⧉ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}نزل + اسم الاغنية او الرابط` ]
⧉ | لتحميل فيديو  ⇦  [ `{HNDLR}نزل فيديو + اسم الاغنية او الرابط` ]
———————×———————

⧉ | لأعاده تشغيل التنصيب أرسل ⇦  [ `{HNDLR}رد شغله` ]
———————×———————
🛠 | @TelethonMusic
⭐ | @LLL5L"""
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!

🎶 هذا ميوزك زوين | @MZAK9
⭐ المطور | @JNUJJ
"""
    await m.reply(REPO, disable_web_page_preview=True)
