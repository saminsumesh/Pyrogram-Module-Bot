from pyrogram import Client, filters
from pyrogram.types import Message


@app.on_message(filters.command("start"))
async def start(app, m: Message):
	await message.reply_text(
		text=f"Hi {message.from_user.mention},\nThis is an simple pyrogram module bot, Free to use and it's opensource,\nIf you find any struggles then Hit /help for a proper knowledge to use this bot,\nFor Source use /source",
		reply_to_message=m.reply_to_message)

@app.on_message(filters.command("help"))
async def help(app, m: Message):
	await message.reply(
		text=Config.HELP_TXT,
		btn = [[
			InlineKeyboardButton("Admin", callback_data="admin"),
			InlineKeyboardButton("Micro", callback_data="micro")
		      ],[
			InlineKeyboardButton("Instance", callback_data="inst"),
			InlineKeyboardButton("Pico", callback_data="pico")
		      ],[
			InlineKeyboardButton("Back", callback_data="start")
		       ]]
		reply_markup=InlineKeyboardMarkup(btn)
	)

@app.on_callback_query()
async def cb_data(app, query):
	if query.data == "start":
		await query.message.edit(
			text=f"Hi {query.from_user.mention},\nThis is an simple pyrogram module bot, Free to use and it's opensource,\nIf you find any struggles then Hit /help for a proper knowledge to use this bot,\nFor Source use /source"
			)
	elif query.data == "close":
		await query.message.delete()
