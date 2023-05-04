import telebot




bot_id = 5050907916

bot = telebot.TeleBot("5853326838:AAFq66AQXrDwJPn-iA9UVnfqFBDhPPTywkI")

 

def send_message(text):
    bot.send_message(text.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['start', 'hello'])
def start_message(message):
    
    bot.send_message(message.chat.id, f"hello")



bot.polling()