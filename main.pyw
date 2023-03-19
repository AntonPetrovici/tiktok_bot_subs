import json
from config import *
import telebot
from donationalerts import Alert


alert = Alert(da_alert_widget_token)
bot = telebot.TeleBot(telebot_token)

def write_json(data, filename='data.json'):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def read_json(filename='data.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def addToList(data):
    list_js = read_json()
    list_js["user_names"].append(data)
    write_json(list_js)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Здравствуйте! Чтобы получить доступ к секретному архиву, оплатите месячную подписку в размере 99₽")
    bot.send_message(message.chat.id, f"Вот ссылка для оплаты: {donate_url} ")
    bot.send_message(message.chat.id, "Отправьте команду /get, когда закончите")

@bot.message_handler(commands=['get'])
def get(message):
    bot.send_message(message.chat.id, "Введите ваше имя из donationalerts, чтобы мы могли удостовериться, что именно вы это вы оплатили подписку")
    bot.register_next_step_handler(message, callback=check_name)
def check_name(message):
    name = message.text
    JS = read_json()
    il = 0
    for item in JS["user_names"]:
        if item == name:
            bot.send_message(message.chat.id, f'Отлично, вы прошли проверку! Вот ссылка на архив: {arhive_link} ')
            break
        elif il >= len(JS["user_names"]) - 1:
            bot.send_message(message.chat.id, "Увы!")
        
        il += 1

            


@alert.event()
def new_donation(event): 
    addToList(event.username)

bot.polling(none_stop=True)








