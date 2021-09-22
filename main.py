import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import datetime
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from telegraph import upload_file
from Config import Config

logging.basicConfig()
logger = logging.getLogger(__name__)

FORCE_SUB = "minregtrgtrrr"

tgraph = Client(
    "Image upload bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
)



@tgraph.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    if Config.FORCE_SUB:
        try:
            chat = await c.get_chat_member(Config.FORCE_SUB, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hey you are kicked from my updates channel. So, you are not able to use me🤣🤣🤣😂😂😂',  quote=True)

        except UserNotParticipant:

            button = [[
                InlineKeyboardButton('BRYLL Bots Updates Channel', url=f'https://t.me/bryllbots')
                ],[
                InlineKeyboardButton('HX Updates Channel', url=f'https://t.me/{Config.FORCE_SUB}')
            ]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="Hey join in my updates channels in order to use me **join fast**👇👇👇.", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            logger.warning(f"Make me admin in @{Config.FORCE_SUB}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{Config.FORCE_SUB}")

        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text("The forcesub username was Incorrect. Please give the correct username.")

        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                if m.from_user.id in Config.AUTH_USERS:
                    return await m.reply_text("Forcesub username must be a channel username Not yours or any other users username")
            logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [our group](https://t.me/HxSupport)", disable_web_page_preview=True, quote=True)



    await m.continue_propagation()






@tgraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention},\nI'm a telegram to telegra.ph image uploader bot by @W4RR10R",
        disable_web_page_preview=True
    )


@tgraph.on_message(filters.photo)
async def getimage(client, message):
    dwn = await message.reply_text("Downloading to my server...", True)
    img_path = await message.download()
    await dwn.edit_text("Uploading as telegra.ph link...")
    try:
        url_path = upload_file(img_path)[0]
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{url_path}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Open Link", url=f"https://telegra.ph{url_path}"
                    ),
                    InlineKeyboardButton(
                        text="Share Link",
                        url=f"https://telegram.me/share/url?url=https://telegra.ph{url_path}",
                    )
                ]
            ]
        )
    )
    os.remove(img_path)


tgraph.run()
