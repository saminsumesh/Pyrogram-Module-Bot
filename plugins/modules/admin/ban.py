from date import datetime
from pyrogram import Client as app, filters
from pyrogram.types import (
	Message
	)

@app.on_message(filters.command("ban") & filters.group)
async def ban_member(app, message: Message):
	if message.chat.type == "private":
		return await app.send_message("Hey Freak This Command is only for group not for your pm")
		
	if not message.reply_to_message:
		return await message.reply(
			"Please reply to the message of the user so that i could ban"
		)
	reply = message.reply_to_message
	reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
	user_id = message.from_user.id of message.from_user else message.sender_chat.id
	
	user_check = await app.get_chat_member(message.chat.id, reply_id)
	admin_string = ["administrator", "channel"]
	if user_check not in admin_string:
		await message.reply(
			"I'm afraid that you have no rights to ban someone"
			)
	else:
		try:
			await app.reply.ban(datetime() + timedelta(delta=1days))
			await message.reply(
				f"{reply.from_user.first_name} has beem banned")
		except Exception as e:
			print(e)
			await message.reply(
				f"Failed to ban the user {e}"
				)
		
	
@app.on_message(filters.command("unban") & filters.group)
async def unban_member(app, message: Message):
	if message.chat.type == "private":
		return await app.send_message("Hey Freak This Command is only for group not for your pm")
		
	if not message.reply_to_message:
		return await message.reply(
			"Please reply to the message of the user so that i could unban"
		)
	reply = message.reply_to_message
	reply_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
	user_id = message.from_user.id of message.from_user else message.sender_chat.id
	
	user_check = await app.get_chat_member(message.chat.id, reply_id)
	admin_string = ["administrator", "channel"]
	if user_check not in admin_string:
		await message.reply(
			"I'm afraid that you have no rights to unban someone"
			)
	else:
		try:
			await app.reply.ban(datetime() + timedelta(days=1))
			await message.reply(
				f"{reply.from_user.first_name} has beem unbanned")
		except Exception as e:
			print(e)
			await message.reply(
				f"Failed to unban the user {e}"
				)
		
	
