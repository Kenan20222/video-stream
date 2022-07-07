# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Salam  Mən səsli söhbətlərdə musiqi oxuda bilən botam 🥰!**

💡 **üzərinə klikləməklə Botun bütün əmrlərini və onların necə işlədiyini öyrənin » 📚 Əmrlər düyməsi!**

🔖 **Bu botdan necə istifadə edəcəyinizi bilmək üçün üzərinə klikləyin » ❓ Əsas Bələdçi düyməsi!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni qrupunza əlavə edin ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Əsas bələdçi", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Əmrlər", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Sahib", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Rəsmi Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Rəsmi Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Bu botdan istifadə üçün əsas əmrlər:**

1.) **Əvvəlcə məni qrupunuza əlavə edin.**
2.) **Sonra məni administrator kimi yüksəldin və Anonim Admindən başqa bütün icazələri verin.**
3.) **Məni təbliğ etdikdən sonra admin məlumatlarını yeniləmək üçün qrupa /reload yazın.**
3.) **Əlavə et @{ASSISTANT_NAME} qrupunuza daxil olun və ya onu dəvət etmək üçün /userbotjoin yazın.**
4.) **Video/musiqi oxutmağa başlamazdan əvvəl video söhbəti yandırın.**
5.) **Bəzən, /reload əmrindən istifadə edərək botu yenidən yükləmək bəzi problemləri həll etməyə kömək edə bilər.**

📌 **İstifadəçi botu video çata qoşulmayıbsa, video çatın artıq aktiv olub olmadığına əmin olun və ya /userbotleave yazın, sonra yenidən /userbotjoin yazın.**

💡 **Bu botla bağlı əlavə suallarınız varsa, onu buradakı dəstək çatımda deyə bilərsiniz: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **izahatı oxumaq və mövcud əmrlərin siyahısına baxmaq üçün aşağıdakı düyməni basın !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Əsas Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Geri Qayıt", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 burada əsas əmrlər var:

» /mplay (mahnı adı/link) - video söhbət musiqi qoyun
» /stream (sorğu/link) - yt canlı/radio canlı musiqini yayımlayın
» /vplay (video adı/link) - video söhbətdə video oynadın
» /vstream - youtube live/m3u8-dən canlı video oynadın
» /playlist - sizə pleylist göstərin
» /video (sual) - youtubedan video yüklə
» /song (sual) - youtubedan mahnı yüklə
» /lyric (sual) - mahnının sözlərini yüklə
» /search (sual) - youtube video linkini axtarın

» /ping - bot ping statusunu göstərin
» /uptime - botun işləmə müddətini göstərin
» /alive - botun canlı məlumatını göstərin (qrupda)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 burada admin əmrləri var:

» /pause - mahnını dayandır
» /resume - mahnını davam eletdir 
» /skip - növbəti musiqiyə keçin
» /stop - musiqini dayandırın
» /vmute - səsli söhbətdə istifadəçi robotunun səsini söndürün
» /vunmute - səsli söhbətdə istifadəçi robotunun səsini açın
» /volume `1-200` - musiqinin səsini tənzimləyin (userbot admin olmalıdır)
» /reload - botu yenidən yükləyin və admin məlumatlarını yeniləyin

» /userbotjoin - istifadəçi robotunu qrupa qoşulmağa dəvət edin
» /userbotleave - userbot-a qrupdan çıxmağı əmr edin

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 burada sudo əmrləri var:

» /rmw - bütün xam faylları təmizləyin
» /rmd - bütün yüklənmiş faylları təmizləyin
» /sysinfo - sistem məlumatlarını göstərin
» /update - botunuzu ən son versiyaya yeniləyin
» /restart - botunuzu yenidən başladın
» /leaveall - userbotun bütün qrupdan çıxmasını əmr edin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri qayıt", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("siz Anonim Adminsiniz!\n\n» admin hüquqlarından istifadəçi hesabına geri qayıdın.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡", yalnız bu düyməyə toxuna bilən səsli söhbətləri idarə etmək icazəsi olan admin!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : musiqini dayandırın\n▶️ : musiqini davam etdirin\n🔇 : istifadəçi robotunu susdur\n🔊 : userbotun səsini açın\n⏹ : musiqini dayandırın",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ hazırda heçnə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡", yalnız bu düyməyə toxuna bilən səsli söhbətləri idarə etmək icazəsi olan admin!", show_alert=True)
    await query.message.delete()
