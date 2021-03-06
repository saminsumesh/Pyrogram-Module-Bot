from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config

BOT_USERNAME = None
BOT_NAME = None
BOT_ID = None
      

class zac(Client):
	
	def __init__(self):
		super().__init__(
			"Pyrogram Module",
			api_id=Config.API_ID,
			api_hash=Config.API_HASH,
			bot_token=Config.BOT_TOKEN,
			workers=50,
			plugins={"root": "plugins"},
			)
			
	async def start(self):
		super().start()
		me = await self.get_me()
		BOT_USERNAME = me.username
		BOT_NAME = me.first_name
		self.username = "@" + me.username
		print(f"{me.first_name} with Pyrogram {__version__}, (Layer {layer}), Started on {me.username}.")
		
	async def stop(self, *args):
		super().stop()
		print("Bot stopped, Bye.")

app = zac()
app.run()
