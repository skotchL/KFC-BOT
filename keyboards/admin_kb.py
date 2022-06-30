from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_load = KeyboardButton("/Yuklash")
button_delete = KeyboardButton('/Bekor_qilish')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)