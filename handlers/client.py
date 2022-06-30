from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
	await bot.send_message(message.from_user.id,"LOL siz /start buyrug'ini berdingiz \n Yordam kerak bo'lsa /help buyrug'idan foydalaning :)", reply_markup=kb_client)


# @dp.message_handler(commands = ['help'])
async def command_help(message : types.Message):
	await bot.send_message(message.from_user.id, "Bizda hozircha mavjud buyruqlar: /start \n /help \n /rejim \n /location")


# @dp.message_handler(commands=['Rejim','rejim'])
async def command_rejim(message: types.Message):
	await bot.send_message(message.from_user.id,"Bizning ish vaqtlarimiz : \n Dush-Shan, 9:00-18:00")

# @dp.message_handler(commands=['location'])
async def command_location(message:types.Message):
	await bot.send_message(message.from_user.id, "Joylashuv : Nomalum ko'cha gala osiyo city 🤓")

#@dp.message_handler(commands=['Menu'])
async def pizza_menu_command(message:types.Message):
	await sqlite_db.sql_read(message)




def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start',])
	dp.register_message_handler(command_help, commands=['help'])
	dp.register_message_handler(command_rejim, commands=['rejim'])
	dp.register_message_handler(command_location, commands=['location'])	
	dp.register_message_handler(pizza_menu_command, commands=['Menu'])