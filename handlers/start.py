import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89cbc8b8760b6abff430f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━
🖤 ʜᴇʏ {message.from_user.mention()} !

         ɪ ᴀᴍ [{bn}](t.me/{bu}) sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs...
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ᴍʏ ᴄᴏᴍᴍᴀɴᴅ ʜᴀɴᴅʟᴇʀs : ( `/ . • $ ^ ~ + * ?` )
┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴄʀᴇᴀᴛᴏʀ: [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](t.me/{OWNER_USERNAME})
┣★
┗━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/{OWNER_USERNAME}) ʙᴀʙʏ...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✗ ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ​ ✗", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "✗ ᴏᴡɴᴇʀ ✗", url=f"https://t.me/{OWNER_USERNAME}"
                    ),
                    InlineKeyboardButton(
                        "✗ sᴜᴘᴘᴏʀᴛ ✗", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "✗ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ ✗", url="https://github.com/AnonymousBoy1025/FallenMusic"
                    )]
            ]
       ),
    )

