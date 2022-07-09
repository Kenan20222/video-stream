# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

from config import BOT_USERNAME
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client, filters
from driver.queues import QUEUE, get_queue
from driver.filters import command, other_filters


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Close", callback_data="cls")]]
)


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "növbə", f"queue@{BOT_USERNAME}"]) & other_filters)
async def playlist(client, m: Message):
   chat_id = m.chat.id
   if chat_id in QUEUE:
      chat_queue = get_queue(chat_id)
      if len(chat_queue)==1:
         await m.reply(f"💡 **Hazırda yayımlanır:**\n\n• [{cat_növbəsi[0][0]}]({cat_növbəsi[0][2]}) | `{cat_növbəsi[0][3]}`", reply_markup=keyboard, disable_web_page_preview=True)
      else:
         QUE = f"💡 **Hazırda yayımlanır:**\n\n• [{chat_queue[0][0]}]({cat_növbəsi[0][2]}) | `{cat_növbəsi[0][3]}` \n\n**📖 Növbə siyahısı:**\n"
         l = len(cat_növbəsi)
         for x in range (1, l):
            han = cat_növbəsi[x][0]
            hok = cat_növbəsi[x][2]
            hap = cat_növbəsi[x][3]
            QUE = QUE + "\n" + f"**#{x}** - [{han}]({hok}) | `{hap}`"
         await m.reply(QUE, reply_markup=keyboard, disable_web_page_preview=True)
   else:
      await m.reply("❌ **hazırda heç nə yayımlanmır.**")
