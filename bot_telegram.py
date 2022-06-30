from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
 

async def on_startup(_):
	print("Bot ishga tushdi, telegramga kirib uni tekshirib ko'ring")
	sqlite_db.sql_start()

from handlers import admin , client

admin.register_handlers_admin(dp) 
client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)