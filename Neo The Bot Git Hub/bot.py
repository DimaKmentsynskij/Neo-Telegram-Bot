'''Dima Kmentsynskyi Lutsk,Ukraine'''
'''The group chat-bot admin'''
'''27.01.2022'''

import telebot
import config
import Filter
import pyowm
import json

from random import randint
from string import punctuation
from time import sleep

bot = telebot.TeleBot(config.TOKEN)

filter = Filter.filter

Phrases_matrix = ['Знати шлях і пройти його – не одне й теж.',
                   'Якби ти не міг прокинутися, як би ти дізнався, що сон, а що дійсність?',
                    '- Не намагайся зігнути ложку. Це неможливо. Спочатку потрібно зрозуміти головне.\n- Що головне?\n- Ложки не існує.\n- Ложки не існує.\n- Не існує?\n— Знаєш, це не ложка гнеться. Все – обман. Справа в тобі.',
                     '— Ти віриш у долю, Нео?\n- Ні.\n- Чому?\n- Неприємно думати, що тобою маніпулюють.',
                      'Відвернися від усього, Нео! Страх, зневіра, сумніви відкинься — очисти свій мозок.',
                       'Слідуй за білим кроликом.',
                        'Час завжди проти нас.',
                         'Знаєте, що я вирішив за десять років, що вільний? Щастя – у незнанні.',
                          'Ти все життя відчував, що світ не гаразд. Дивна думка, але її не відігнати. Вона - як скалка в мозку. Вона зводить з розуму, не дає спокою. Це і привело тебе до мене.',
                           'Ти загруз у Матриці...',
                            'Дядько чарівник, забирай мене звідси!',
                             'Я знаю кунг-фу.',
                              'Ви всі живете у світі мрій.',
                               'Твій вибір уже зроблено. Тобі лишається його усвідомити.',
                                'Краще ворушити мізками, ніж програвати м\'язами.',
                                 'Вибір. Проблема у виборі.',
                                  'Будь-яка історія може мати два фінали.',
                                   'Заперечення - звичайнісінька з людських реакцій.',
                                    'Хіба ти обирати до мене прийшов? Твій вибір зроблено. Ти намагаєшся зрозуміти, чому ти його зробив.',
                                     'Прямота - ознака щирості.',
                                      'Будь-яка програма створюється з якоюсь метою. В іншому випадку вона стирається.']
con = [
       "congrats/1.jpg",
        "congrats/2.jpg",
         "congrats/3.jpg",
          "congrats/4.jpg",
           "congrats/5.jpg",
            "congrats/6.jpg",
             "congrats/7.jpg",
              "congrats/8.jpg",
               "congrats/9.jpg",
                "congrats/10.jpg",
                 "congrats/11.jpg",
                  "congrats/12.jpg",
                   "congrats/13.jpg",
                    "congrats/14.jpg",
                     "congrats/15.jpg",
                      "congrats/16.jpg",
                       "congrats/17.jpg",
                        "congrats/18.jpg",
                         "congrats/19.jpg",
                          "congrats/20.jpg",
                           "congrats/22.jpg",
                            "congrats/23.jpg",
                             "congrats/24.jpg",
                              "congrats/25.jpg",
                               "congrats/26.jpg",
                                "congrats/27.jpg",
                                 "congrats/28.jpg",
                                  "congrats/29.jpg",
                                   "congrats/30.jpg",
                                    "congrats/31.jpg",
                                     "congrats/32.jpg",
                                      "congrats/33.jpg",
                                       "congrats/34.jpg",]

@bot.message_handler(commands=['dice'])
def matrix(message):
     bot.send_dice(message.chat.id, "🎲")

@bot.message_handler(commands=['spin'])
def matrix(message):
     bot.send_dice(message.chat.id, "🎰")

@bot.message_handler(commands=['throwball'])
def ball(message):
     bot.send_dice(message.chat.id, "🏀")

@bot.message_handler(commands=['dartz'])
def ball(message):
     bot.send_dice(message.chat.id, "🎯")

@bot.message_handler(commands=['quote_matrix'])
def matrix(message):
     bot.send_message(message.chat.id, Phrases_matrix[randint(0, 20)])

@bot.message_handler(commands=['congrat'])
def congrarulations(message):
    photo = open(con[randint(0, 32)], 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['gayness'])
def gayness(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, f"{name} " + str(randint(0, 100)) + "% gay!🏳‍🌈")

@bot.message_handler(commands=['weather'])
def dice(message):
     city = "Lutsk, UA"
     owm = pyowm.OWM("188540f4b0036ade07b9f35c635ad6fc")
     mgr = owm.weather_manager()
     observation = mgr.weather_at_place(city)
     w = observation.weather
     temp = w.temperature('celsius')['temp']
     bot.send_message(message.chat.id, "У Луцьку🏢 " + " зараз " + str(round(temp, 1)) + "°C🌥️")

@bot.message_handler(commands=['rules'])
def rules(message):
    bot.send_message(message.chat.id, '''Ось правила секретного колективу:
1) заборонено хамити😠

2) заборонено ображати інших учасників групи😢.

3) заборонено використовувати нецензурну лексику🤬.

4) заборонено надсилати посилання реклами💯.

5) сваритись і провокувати співбесідника в чаті недопустимо☠️.

Тож в тебе є вибір:  
🔵💊синя таблетка дотримуватися правил; 
🔴💊червона таблетка бути забаненим☠️''')

@bot.message_handler(commands=['whoisbot'])
def whoisbot(message):
    bot.send_message(message.chat.id, '''Я агент під прикриттям🕴, своє ім'я я не можу називати.

І я працюю на корпорацію "чт*т/и отрезала руку"😁.

 Я був створений, щоб допомагати🤝 адміністрації.

Якщо у вас виникло запитання❓ навіщо я створений для простих людей, то:
я видаляю❌ повідомлення, які порушують правила спільноти, їх можна подивитись написавши команду "/rules";

 виконую команди🐶;

 слідкую за порядком👮;

 і бажаю вам гарного відпочинку🌿.''')

@bot.message_handler()
def chatting(message):
    if {i.lower().translate(str.maketrans('','', punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('filter.json')))) != set():
        bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True)
