from pyrogram import Client, filters
from pyrogram.types import Message


@app.on_message(filters.command("start"))
async def start(app, m: Message):
	await message.reply_text(
		text=f"Hi {},\nThis is an simple pyrogram module bot, Free to use and it's opensource,\nIf you find any struggles then Hit /help for a proper knowledge to use this bot,\nFor Source use /source",
		reply_to_message=m.reply_to_message)

@app.on_message(filters.command("help"))
async def help(app, m: Message):
	# need to fill accordingly to the bots plugins
      # undefined project
      # time to modules.
