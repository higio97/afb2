import config
from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


async def belicoin_handler(client: Client, msg: Message):
    url = config.topup_link
    owner_username = f"t.me/{config.admin_username}"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🏧 Beli disini", url=url)],
            [InlineKeyboardButton("📨 Konfirmasi", url=owner_username)],
        ]
    )

    await msg.reply_photo(config.pic_main, caption=config.pesan_topup, reply_markup=keyboard)
