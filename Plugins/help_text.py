
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import filters
from bot import autocaption
from config import Config
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
 

#all buttons 

#start buttons 

start_button=InlineKeyboardMarkup(
        [
             
              [
                  InlineKeyboardButton("Help", callback_data = Help_user"), 
                  InlineKeyboardButton("About", callback_data = "about_text")
              ], 
              [
                  InlineKeyboardButton("Nexon Projects ❤", Url = "https"//telegram.me/Nexonhex")
              ],
              [
                  InlineKeyboardButton("Dev", url = "https://telegram.me/itz_me_shon"), 
                  InlineKeyboardButton("Support", url = "https://telegram.me/Nexonhex_grp")
              ] 
        ]
)

# help buttons

help_button=InlineKeyboardMarkup(
        [
              [
                InlineKeyboardButton("Support", url = "https://telegram.me/nexonhex_grp")
              ], 
              
        ]

) 

# about button

about_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("Dev", url = "https://telegram.me/itz_me_shon"), 
                  InlineKeyboardButton("support", url = "https://telegram.me/nexonhex_grp")
              ]
        ]
) 

@client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.START_TEXT.format(cmd.from_user.first_name, Config.ADMIN_USERNAME), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@client.on_message(filters.command("help") & filters.private)
async def help(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "html",
          disable_web_page_preview = True,
          reply_markup = help_button           
      )


@client.on_message(filters.command("about") & filters.private)
async def about(bot, cmd):
      await bot.send_message(
          chat_id = cmd.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = about_button
      )



# call_backs 

@client.on_callback_query()
async def button(bot, cmd: CallbackQuery):
    cb_data = cmd.data
    if "about_data" in cb_data:
        await cmd.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode="markdown", 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("Dev", url="https://telegram.me/itz_me_shon"),
                      InlineKeyboardButton("support", url="https://telegram.me/nexonhex_grp")
                     ]
 
                 ] 
             ) 
        )
    
