import os, logging, time, string, traceback, datetime
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from Config import Config

logging.basicConfig()
logger = logging

FORCE_SUB = Config.FORCE_SUB1
FORCE_SUB2 = Config.FORCE_SUB2

tgraph = Client(
    "Bryll Education Bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
)

AUTH_USERS = [185207002, 1033516714, 1105888249, 800219239]

start_keyboard = ReplyKeyboardMarkup([['🎓 Subjects 🎓', 'start the bot']], resize_keyboard=True)

force_sub_keyboard = ReplyKeyboardMarkup([
     ['BRYLL Bots Updates Channel'],
     ['Updates Channel', 'Bryll EDU']], resize_keyboard=True)


premuim_pay_keyboard = ReplyKeyboardMarkup([['Contact Our Helpdesk']], resize_keyboard=True)

subjects_keyboard = ReplyKeyboardMarkup([['🩺 Biology ☣', '🥏 Physics🌀'],
     ['🧬 Chemistry 🔬']], resize_keyboard=True)


CCHAPTER_BTN = [
    [InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/beyllbots')],
    [InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')]]


PCHAPTER_BTN = [
    [InlineKeyboardButton('Chapter 01', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('Chapter 02', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')]]

BCHAPTER_BTN = [
    [InlineKeyboardButton('Chapter 01', url=f'https://d2bps9p1kiy4ka.cloudfront.net/5eb393ee95fab7468a79d189/50c941fa-52bc-4714-9cc3-e1af8b86b590.pdf')],
    [InlineKeyboardButton('Chapter 02', callback_data='bch1_cd')],
    [InlineKeyboardButton('Chapter 03', url=f'https://telegram.me/bryllbots')],
    [InlineKeyboardButton('⏪ Back ⏪', callback_data='subject_cd')]]



@tgraph.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    message = m
    if message.text == "BRYLL Bots Updates Channel": await message.reply_text("@bryllbots", reply_to_message_id=message.message_id)
    elif message.text == "Updates Channel": await message.reply_text(f'@{Config.FORCE_SUB1}', reply_to_message_id=message.message_id)
    elif message.text == "Bryll EDU": await message.reply_text(f'@{Config.FORCE_SUB2}', reply_to_message_id=message.message_id)
    elif message.text == "Contact Our Helpdesk": await message.reply_text("@bryll_helpdesk_bot", reply_to_message_id=message.message_id)
    elif message.text == "start the bot": await message.reply_text("bot is started now choose any thing to see more")

    if Config.FORCE_SUB1 != "":
        try:
            chat = await c.get_chat_member(Config.FORCE_SUB1, m.from_user.id)
            if Config.FORCE_SUB2 != "":
               chat2 = await c.get_chat_member(Config.FORCE_SUB2, m.from_user.id)
            print("ok")
            if chat.status=='kicked' or chat2.status=='kicked':
                return await m.reply_text('Hey you are kicked from my updates channel. So, you are not able to use me🤣🤣🤣😂😂😂',  quote=True)

        except UserNotParticipant:
            print("not ok")
            button = [[
                InlineKeyboardButton('BRYLL Bots Updates Channel', url=f'https://t.me/bryllbots')
                ],[
                InlineKeyboardButton('Updates Channel', url=f'https://t.me/{Config.FORCE_SUB1}')
                ],[
                InlineKeyboardButton('Bryll EDU', url=f'https://t.me/{Config.FORCE_SUB2}')
                ],[
                InlineKeyboardButton('🔄 Refresh 🔄', callback_data='refresh')
            ]]
            markup = force_sub_keyboard
            return await m.reply_text(text=f"Hey! {m.from_user.mention(style='md')} join order to use me **join fast**👇👇👇.", parse_mode='markdown', reply_markup=markup, quote=True)


        except ChatAdminRequired:
            print("admin")
            logger.warning(f"Make me admin in @{Config.FORCE_SUB1}")


        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")


        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")

            logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [our group](https://t.me/bryllbots_support)", disable_web_page_preview=True, quote=True)



    await m.continue_propagation()






@tgraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello {message.from_user.mention},\nI'm a telegram 🎓 Education Bot From BRYLL EDUCATION Group \nMade with ❤ by @bryllbots",
        disable_web_page_preview=True,
        reply_markup = start_keyboard)


@tgraph.on_message(filters.regex("🎓 Subjects 🎓"))
async def subject(client,message):
    if message.from_user.id not in AUTH_USERS:
        await message.reply_text(
            text=f"**Hey {message.from_user.mention}!\n\n👉 You have not purchased our premium plan. To use this command kindly purchase our premium plan.\n\n👉 Details of the premium plan👇👇👇\n999 Rs. + 18% GST\n\nIf you are interested in our service then you can buy the plan by contacting our helpdesk👇👇👇**",
            reply_markup = premuim_pay_keyboard)
        return
    await message.reply_text(
        text=f"Hey! Choose the Subject",
        disable_web_page_preview=True,
        reply_markup = subjects_keyboard)



@tgraph.on_message(filters.regex("🩺 Biology ☣"))
async def biology(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
    )


@tgraph.on_message(filters.regex("🥏 Physics 🌀"))
async def physics(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
     )


@tgraph.on_message(filters.regex("🧬 Chemistry 🔬"))
async def chemistry(client,message):
    await message.reply_text(
        text=f"Hey! {message.from_user.mention} Choose the Chapter which you want to study",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(CCHAPTER_BTN)
    )


@tgraph.on_message(filters.regex("me"))
async def me(client,message):
    await message.reply_text(
        text=f"""**Your Details**

**First Name:-** <code>{message.from_user.first_name}</code>

**Last Name:-** <code>{message.from_user.last_name}</code>

**User Name:-** @{message.from_user.username}

**User ID:-** <code>{message.from_user.id}</code>""",
        disable_web_page_preview=True,
      )



@tgraph.on_message(filters.command("bio"))
async def bio(client, message):
    await tgraph.copy_messages(chat_id=message.from_user.id, from_chat_id=-1001430997268, message_ids=2)
    




@tgraph.on_callback_query()
async def cd_handler(bot, update):
    if update.data =="subject_cd":
        await update.message.edit_text(
            text=f"Hey! {update.from_user.mention} Choose the Subject",
            disable_web_page_preview=True,
            reply_markup=subjects_keyboard)
    # elif update.data =="biology_cd":
    #     await update.message.edit_text(
    #         text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Biology",
    #         disable_web_page_preview=True,
    #         reply_markup=InlineKeyboardMarkup(BCHAPTER_BTN)
    #       )
    # elif update.data == "physics_cd":
    #     await update.message.edit_text(
    #          text=f"Hey! {update.from_user.mention} Choose the Chapter which you want to study in Physics",
    #          disable_web_page_preview=True,
    #          reply_markup=InlineKeyboardMarkup(PCHAPTER_BTN)
    #        )
    # elif update.data =="chemistry_cd":
    #     await update.message.edit_text(
    #         text=f"Hey! {update.from_user.mention} Choose the Chapter which you wany to study in Chemistry",
    #         disable_web_page_preview=True,
    #         reply_markup=InlineKeyboardMarkup(CCHAPTER_BTN)
    #      )
    
    elif update.data =="bch1_cd":
        msg_content = await bot.get_messages(chat_id=-1001430997268, message_ids=2)
        await msg_content.forward(chat_id=update.from_user.id)
    elif update.data =="refresh":

        try:
            chat = await bot.get_chat_member(Config.FORCE_SUB1, update.from_user.id)
            chat2 = await bot.get_chat_member(Config.FORCE_SUB2, update.from_user.id)


            if chat.status=='kicked' or chat.status=='kicked':
               return await update.reply_text('Hey you are kicked from my update channel. So, you are not able to use me🤣🤣🤣😂😂😂', quote=True)

        except UserNotParticipant:
            markup = force_sub_keyboard
            return await update.answer(text=f"I told you to join my updates channel. Join the updates channel then send me message.", show_alert=True)

        await update.message.edit_text(
            text=f"Hello {update.from_user.mention},\nI'm a telegram Education Bot From BRYLL EDUCATION bot by @bryllbots",
            disable_web_page_preview=True,
            reply_markup=start_keyboard)

    elif update.data =="close":
         await update.message.delete()


tgraph.run()
