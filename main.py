import os
import logging
from pyrogram import Client, filters
import datetime
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
            

        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            

        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                
            logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [our group](https://t.me/HxSupport)", disable_web_page_preview=True, quote=True)



    await m.continue_propagation()






@tgraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention},\nI'm a telegram to telegra.ph image uploader bot by @W4RR10R",
        disable_web_page_preview=True
    )

@tgraph.on_message(filters.command("subject"))
async def subject(client,message):
    await message.reply_text(
        text=f"Hey! Choose the Subject",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(SUBJECT_BTN)
        )

SUBJECT_BTN = [[
    InlineKeyboardButton('Biology', callback_data='biology_cd')
    ],[
    InlineKeyboardButton('Physics', callback_data='physics_cd')
    ],[
    InlineKeyboardButton('Chemistry', url=f'https://telegram.me/bryllbots')
    ]]
                        

@tgraph.on_message(filters.command("biology"))
async def biology(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
    )
    
BCHAPTER_BTN = [[
     InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')
     ],[
     InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/bryllbots')
     ],[
     InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
     ]]

@tgraph.on_message(filters.command("physics"))
async def physics(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
     )
    
PCHAPTER_BTN = [[
      InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')
      ],[
      InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/bryllbots')
      ],[
      InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
      ]]


@tgraph.on_message(filters.command("chemistry"))
async def chemistry(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(CCHAPTER_BTN)
    )
    
CCHAPTER_BTN = [[
       InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')
       ],[
       InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/beyllbots')
       ],[
       InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')
       ]]
    


@tgraph.on_callback_query()
async def cd_handler(bot, update):
    if update.data =="biology_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Biology",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
          )
      else update.data == "physics_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Biology",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
          )
    
tgraph.run()
