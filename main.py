import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

# Khởi tạo bot
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


# Định nghĩa trình xử lý lệnh start
@bot.message_handler(commands=['start'])
def start(message):
  # Tạo một nút bàn phím inline
  button = types.InlineKeyboardButton(
      "Play Game",
      web_app=types.WebAppInfo(url="https://shrub-aquatic-kidney.glitch.me/"))
  # Tạo một đánh dấu bàn phím inline với nút
  keyboard = types.InlineKeyboardMarkup().add(button)
  # Gửi một thông điệp với bàn phím inline
  with open('logo.jpg', 'rb') as photo:
    bot.send_photo(message.chat.id,
                   photo,
                   "Race a car to earn your gem, get your airdrop",
                   reply_markup=keyboard)


# Bắt đầu bot
bot.polling()
