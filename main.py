import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup


TOKEN = '***'
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
        datepon = ponbs.find(string='Понедельник').parent
        date2pon = datepon.get_text()
        isip20pon = ponbs.find('td', string='ИСиП-20').parent
        td_count=-1
        for td in isip20pon.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')
        temppon = isip20pon.text
        #team = temppon.split('\n')
        #dd3pon = [a.replace('ИСиП-20', '').replace('\xa0', 'окно') for a in team]
        #for i in range(len(dd3pon) - 1):
            #if dd3pon[i] == dd3pon[i + 1]:
                #del dd3pon[i + 1]
            #elif dd3pon[i] == '':
                #dd3pon.insert(i + 1, "\n")

        #print(dd3pon)
        #dd3pon=list(filter(lambda x: x != '', dd3pon))
        #print(dd3pon)
        #result = " ".join(dd3pon).strip()
        #print(result)
        daspon = [temppon]
        dd2pon = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно') for a in daspon]
        hipon = ' '.join(dd2pon)
        date3pon = date2pon.replace('Понедельник', '').strip()
        hi2pon = hipon.strip().replace('  ', '')
        gspon = date3pon + '\n' + '\n' + hi2pon
        #gspon2 = date3pon + '\n' + result
        bot.send_message(message.chat.id, text=(gspon))
    elif (message.text == "Вторник"):
        responsevtor = requests.get(vtor)
        vtorbs = BeautifulSoup(responsevtor.text, "lxml")
        datevtor = vtorbs.find(string='Вторник').parent
        date2vtor = datevtor.get_text()
        isip20vtor = vtorbs.find('td', string='ИСиП-20').parent
        td_count = -1
        for td in isip20vtor.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')
        tempvtor = isip20vtor.text
        dasvtor = [tempvtor]
        dd2vtor = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\r', '') for a in dasvtor]
        hivtor = ' '.join(dd2vtor)
        date3vtor = date2vtor.replace('Вторник', '').strip()
        hi2vtor = hivtor.strip().replace('  ', '')
        gsvtor = date3vtor + '\n' '\n' + hi2vtor
        bot.send_message(message.chat.id, text=(gsvtor))
    elif (message.text == "Среда"):
        responsecreda = requests.get(creda)
        credabs = BeautifulSoup(responsecreda.text, "lxml")
        datecreda = credabs.find(string='Среда').parent
        date2creda = datecreda.get_text()
        isip20creda = credabs.find('td', string='ИСиП-20').parent
        td_count = -1
        for td in isip20creda.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')

        tempcreda = isip20creda.text
        dascreda = [tempcreda]
        dd2creda = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\r', '') for a in
                   dascreda]
        hicreda = ' '.join(dd2creda)
        date3creda = date2creda.replace('Среда', '').strip()
        hi2creda = hicreda.strip().replace('  ', '')
        gscreda = date3creda + '\n' + '\n' + hi2creda
        bot.send_message(message.chat.id, text=(gscreda))
    elif (message.text == "Четверг"):
        responsechet = requests.get(chetwerk)
        chetbs = BeautifulSoup(responsechet.text, "lxml")
        datechet = chetbs.find(string='Четверг').parent
        date2chet = datechet.get_text()
        isip20chet = chetbs.find('td', string='ИСиП-20').parent
        td_count = -1
        for td in isip20chet.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')
        tempchet = isip20chet.text
        daschet = [tempchet]
        dd2chet = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\r', '') for a in
                    daschet]
        hichet = ' '.join(dd2chet)
        date3chet = date2chet.replace('Четверг', '').strip()
        hi2chet = hichet.strip().replace('  ', '')
        gschet = date3chet + '\n' +  "\n" + hi2chet
        bot.send_message(message.chat.id, text=(gschet))
    elif (message.text == "Пятница"):
        responsepyat = requests.get(pyat)
        pyatbs = BeautifulSoup(responsepyat.text, "lxml")
        datepyat = pyatbs.find(string='Пятница').parent
        date2pyat = datepyat.get_text()
        isip20pyat = pyatbs.find('td', string='ИСиП-20').parent
        td_count = -1
        for td in isip20pyat.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')
        temppyat = isip20pyat.text
        daspyat = [temppyat]
        dd2pyat = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\r', '') for a in
                   daspyat]
        hipyat = ' '.join(dd2pyat)
        date3pyat = date2pyat.replace('Пятница', '').strip()
        hi2pyat = hipyat.strip().replace('  ', '')
        gspyat = date3pyat + '\n'+ '\n' + hi2pyat
        bot.send_message(message.chat.id, text=(gspyat))
    elif (message.text == "Суббота"):
        responsesub = requests.get(subbota)
        subbs = BeautifulSoup(responsesub.text, "lxml")
        datesub = subbs.find(string='Суббота дистанционно').parent
        date2sub = datesub.get_text()
        isip20sub = subbs.find('td', string='ИСиП-20').parent
        td_count = -1
        for td in isip20sub.find_all('td'):
            td_count += 1
            if td_count % 2 == 1:
                td.insert_after('\n')
        tempsub = isip20sub.text
        dassub = [tempsub]
        dd2sub = [a.replace('ИСиП-20', '').replace('\xa0\n\xa0', 'окно').replace('\r', '') for a in
                   dassub]
        hisub = ' '.join(dd2sub)
        date3sub = date2sub.replace('Суббота дистанционно', '').strip()
        hi2sub = hisub.strip().replace('  ', '')
        gssub = date3sub + '\n' + '\n' + hi2sub
        bot.send_message(message.chat.id, text=(gssub))
bot.polling(none_stop=True)