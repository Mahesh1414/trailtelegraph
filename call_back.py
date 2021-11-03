import os
import logging
import time
import string
import traceback
from pyrogram import Client, filters
import datetime
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from Config import Config

logging.basicConfig()
logger = logging.getLogger(__name__)


@tgraph.on_callback_query()
async def cd_handler(bot, update):
    if update.data =="subject_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Subject",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(SUBJECT_BTN)
          )
    elif update.data =="biology_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Biology",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
          )
    elif update.data == "physics_cd":
        await update.message.edit_text(
             text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Physics",
             disable_web_page_preview=True,
             reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
           )
    elif update.data =="chemistry_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Chapter which you wany to study in Chemistry",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(CCHAPTER_BTN)
          )
    elif update.data =="bch1_cd":
        await update.message.edit_text(
            text=f"""<b>Lakshya NEET Batch PW🎯🎯🎯
Biology
Microbes in Human Welfare
Lecture 03
Lecture🔰
👉 https://d1d34p8vz63oiq.cloudfront.net/9eb5c7a1-611c-40ac-b7a8-d07dc56b5304/master.m3u8
Class Notes🔰
👉 https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/50c941fa-52bc-4714-9cc3-e1af8b86b590.pdf
DPP🔰
👉 https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/5b193fd6-9d46-4f43-80fe-530f4cd767e6.pdf
🦧 Use @bryll_urluploader_bot to download Lecture. 🦦
For any help contact💬 @bryll_helpdesk_bot</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
          )
    elif update.data =="refresh":
        try:
            chat = await bot.get_chat_member(Config.FORCE_SUB, update.from_user.id)

            if chat.status=='kicked':
               return await update.reply_text('Hey you are kicked from my update channel. So, you are not able to use me🤣🤣🤣😂😂😂', quote=True)

        except UserNotParticipant:
            
            button = [[
                InlineKeyboardButton('BRYLL Bots Updates Channel', url=f'https://t.me/bryllbots')
                ],[
                InlineKeyboardButton('Updates Channel', url=f'https://t.me/{Config.FORCE_SUB}')
                ],[
                InlineKeyboardButton('🔄 Refresh 🔄', callback_data='refresh')
            ]]
            markup = InlineKeyboardMarkup(button)
            return await update.answer(text=f"I told you to join my updates channel. Join the updates channel then send me message.", show_alert=True)

        await update.message.edit_text(
              text=f"Hello {message.from_user.mention},\nI'm a telegram Education Bot From BRYLL EDUCATION bot by @bryllbots",
              disable_web_page_preview=True,
              reply_markup=InlineKeyboardMarkup(START_BTN))

    elif update.data =="close":
         await update.message.delete()
