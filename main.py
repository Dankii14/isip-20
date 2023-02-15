import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup


TOKEN = '**'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Понедельник")
    btn2 = types.KeyboardButton("Вторник")
    btn3 = types.KeyboardButton("Среда")
    btn4 = types.KeyboardButton("Четверг")
    btn5 = types.KeyboardButton("Пятница")
    btn6 = types.KeyboardButton("Суббота")

    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)

    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для расписания".format(
                         message.from_user), reply_markup=markup)


pon = 'https://utmiit.ru/ZR/ZR1.htm'
vtor = 'https://utmiit.ru/ZR/ZR2.htm'
creda = 'https://utmiit.ru/ZR/ZR3.htm'
chetwerk = 'https://utmiit.ru/ZR/ZR4.htm'
pyat = 'https://utmiit.ru/ZR/ZR5.htm'
subbota = 'https://utmiit.ru/ZR/ZR6.htm'
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Понедельник"):
        responsepon = requests.get(pon)
        ponbs = BeautifulSoup(responsepon.text, "lxml")
        datepon = ponbs.find(text='Понедельник').parent
        date2pon = datepon.get_text()
        isip20pon = ponbs.find('td', text='ИСиП-20').parent
        temppon = isip20pon.text
        daspon = [temppon]
        dd2pon = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in daspon]
        hipon = ' '.join(dd2pon)
        date3pon = date2pon.replace('Понедельник', '').strip()
        hi2pon = hipon.strip().replace('  ', '')
        gspon = date3pon + '\n' + hi2pon
        bot.send_message(message.chat.id, text=(gspon))
    elif (message.text == "Вторник"):
        responsevtor = requests.get(vtor)
        vtorbs = BeautifulSoup(responsevtor.text, "lxml")
        datevtor = vtorbs.find(text='Вторник').parent
        date2vtor = datevtor.get_text()
        isip20vtor = vtorbs.find('td', text='ИСиП-20').parent
        tempvtor = isip20vtor.text
        dasvtor = [tempvtor]
        dd2vtor = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in dasvtor]
        hivtor = ' '.join(dd2vtor)
        date3vtor = date2vtor.replace('Вторник', '').strip()
        hi2vtor = hivtor.strip().replace('  ', '')
        gsvtor = date3vtor + '\n' + hi2vtor
        bot.send_message(message.chat.id, text=(gsvtor))
    elif (message.text == "Среда"):
        responsecreda = requests.get(creda)
        credabs = BeautifulSoup(responsecreda.text, "lxml")
        datecreda = credabs.find(text='Среда').parent
        date2creda = datecreda.get_text()
        isip20creda = credabs.find('td', text='ИСиП-20').parent
        tempcreda = isip20creda.text
        dascreda = [tempcreda]
        dd2creda = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in
                   dascreda]
        hicreda = ' '.join(dd2creda)
        date3creda = date2creda.replace('Среда', '').strip()
        hi2creda = hicreda.strip().replace('  ', '')
        gscreda = date3creda + '\n' + hi2creda
        bot.send_message(message.chat.id, text=(gscreda))
    elif (message.text == "Четверг"):
        responsechet = requests.get(chetwerk)
        chetbs = BeautifulSoup(responsechet.text, "lxml")
        datechet = chetbs.find(text='Четверг').parent
        date2chet = datechet.get_text()
        isip20chet = chetbs.find('td', text='ИСиП-20').parent
        tempchet = isip20chet.text
        daschet = [tempchet]
        dd2chet = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in
                    daschet]
        hichet = ' '.join(dd2chet)
        date3chet = date2chet.replace('Четверг', '').strip()
        hi2chet = hichet.strip().replace('  ', '')
        gschet = date3chet + '\n' + hi2chet
        bot.send_message(message.chat.id, text=(gschet))
    elif (message.text == "Пятница"):
        responsepyat = requests.get(pyat)
        pyatbs = BeautifulSoup(responsepyat.text, "lxml")
        datepyat = pyatbs.find(text='Пятница').parent
        date2pyat = datepyat.get_text()
        isip20pyat = pyatbs.find('td', text='ИСиП-20').parent
        temppyat = isip20pyat.text
        daspyat = [temppyat]
        dd2pyat = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in
                   daspyat]
        hipyat = ' '.join(dd2pyat)
        date3pyat = date2pyat.replace('Пятница', '').strip()
        hi2pyat = hipyat.strip().replace('  ', '')
        gspyat = date3pyat + '\n' + hi2pyat
        bot.send_message(message.chat.id, text=(gspyat))
    elif (message.text == "Суббота"):
        responsesub = requests.get(subbota)
        subbs = BeautifulSoup(responsesub.text, "lxml")
        datesub = subbs.find(text='Суббота дистанционно').parent
        date2sub = datesub.get_text()
        isip20sub = subbs.find('td', text='ИСиП-20').parent
        tempsub = isip20sub.text
        dassub = [tempsub]
        dd2sub = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\n', ' ').replace('\r', '') for a in
                   dassub]
        hisub = ' '.join(dd2sub)
        date3sub = date2sub.replace('Суббота дистанционно', '').strip()
        hi2sub = hisub.strip().replace('  ', '')
        gssub = date3sub + '\n' + hi2sub
        bot.send_message(message.chat.id, text=(gssub))
bot.polling(none_stop=True)