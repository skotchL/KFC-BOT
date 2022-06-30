from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb

ID = None


class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	description = State()
	price = State()

# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message:types.Message):
	global ID 
	ID = message.from_user.id
	await bot.send_message(message.from_user.id, 'Nima kerak ?', reply_markup = admin_kb.button_case_admin)


# @dp.message_handler(state="*", commands='Bekor qilish')
# @dp.message_handler(Text(equals='Bekor qilish', ignore_case=True), state="*")	
async def cancel_handler(message:types.Message, state:FSMContext):
	if message.from_user.id == ID:
		current_state = await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.reply("OK")


# @dp.message_handler(commands='Yuklash', state=None)
async def cm_start(message: types.Message):
	await FSMAdmin.photo.set()
	await message.reply('Rasm yuklash')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply('Ismini kiritings')

# @dp.message_handler(state =FSMAdmin)
async def load_name(message:types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply('Description kiriting')

# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['description'] = message.text
	await FSMAdmin.next()
	await message.reply("Narxini kiriting")

# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state:FSMContext):
	async with state.proxy() as data:
		data['price'] = float(message.text)

	async with state.proxy() as data:
		await message.reply(str(data))
		await sqlite_db.sql_add_command(state)

	await state.finish()



def register_handlers_admin(dp: Dispatcher):
	dp.register_message_handler(cm_start, commands=['Yuklash'], state=None)
	dp.register_message_handler(cancel_handler, state="*", commands='Bekor_qilish')
	dp.register_message_handler(cancel_handler, Text(equals='Bekor_qilish', ignore_case=True), state="*")
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)	
	dp.register_message_handler(load_description, state=FSMAdmin.description)
	dp.register_message_handler(load_price, state=FSMAdmin.price)
	dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)