from pyrogram import Client as app, filters
from pyrogram.types import (
	Message,
	InlineKeyboardButton,
	InlineKeyboardMarkup
	)
from helpers.admin.admin_func import admin_check

@app.on_message(filters.command("pin"))
async def pin(app, message: Message):
	if not message.chat.type == "private":
		await app.send_message(
			message.chat.id,
			text="**This command is only for group not for your pm**",
			reply_to_message=message.id
		)
		return     
	if not message.reply_to_message:
		return await message.reply("Please reply to a message"
		)

	reply = message.reply_to_message
	reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
	user_id = message.from_user.id if message.from_user else message.sender_chat.id
	
	user_status = await app.get_chat_member(message.chat.id, user_id)
	admin_string = ["administrator", "creator"]
	if user_status not in admin_string:
		await message.reply("I'm afraid that you are not an admin **Here**")
	else:
		try:
			await app.reply.pin()
		except Exception as e:
			print(e)
			await message.reply(f"Failed to pin your message {e}")
		
		
