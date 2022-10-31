import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/release/anekdot/year/'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

lists_of_jokes = parser(URL)
random.shuffle(lists_of_jokes)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands =['начать'])

def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Чтобы посмеяться ввeдите любую цифру:')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '1234567890':
        bot.send_message(message.chat.id, lists_of_jokes[0])
        del lists_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Ввeдите любую цифру:')

bot.polling()
