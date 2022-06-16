import requests
from datetime import datetime
import telebot
from telebot import types
from auth_data import token

def TELEGRAM_BOT(token):
    bot = telebot.TeleBot(token)

    def buttons():
        global markup2, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b1 =  types.KeyboardButton(text = 'BTC')
        b2 =  types.KeyboardButton(text = 'ETH')
        b3 =  types.KeyboardButton(text = 'BNB')
        b4 =  types.KeyboardButton(text = 'XRP')
        b5 =  types.KeyboardButton(text = 'DOGE')
        b6 = types.KeyboardButton(text = 'MANA')
        b7 = types.KeyboardButton(text = 'MATIC')
        b8 = types.KeyboardButton(text = 'LTC')
        b9 = types.KeyboardButton(text = 'LINK')
        b10 = types.KeyboardButton(text = 'TRX')

        markup2.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello, my name is Mr McQuack))\nПривет, меня зовут Скрудж Макдак')
        markup1 = types.InlineKeyboardMarkup()
        bl1 = types.InlineKeyboardButton(text = 'Русский', callback_data='ru')
        bl2 = types.InlineKeyboardButton(text = 'English', callback_data='en')
        markup1.add(bl1, bl2)
        bot.send_message(message.chat.id, 'Choose the language\nВыберите язык', reply_markup = markup1)


    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'en':
            global l
            l = 'en'
            buttons()
            bot.send_message(call.message.chat.id, 'Choose your coin', reply_markup = markup2)

            @bot.message_handler(content_types=['text'])
            def callback1(message):
                if message.text == 'BTC':
                    req = requests.get(f'https://yobit.net/api/3/ticker/btc_usd')
                    response = req.json()
                    prc = response['btc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nBitcoin[BTC] price: ${prc}')
                elif message.text == 'ETH':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/eth_usd')
                    response = req.json()
                    prc = response['eth_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nEthereum[ETH] price: ${prc}')
                elif message.text == 'BNB':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/bnbbsc_usd')
                    response = req.json()
                    prc = response['bnbbsc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nBNB[BNB] price: ${prc}')
                elif message.text == 'XRP':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/xrp_usd')
                    response = req.json()
                    prc = response['xrp_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nXRP[XRP] price: ${prc}')
                elif message.text == 'DOGE':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/doge_usd')
                    response = req.json()
                    prc = response['doge_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nDogecoin[DOGE] price: ${prc}')
                elif message.text == 'MATIC':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/matic_usd')
                    response = req.json()
                    prc = response['matic_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nPolygon[MATIC] price: ${prc}')
                elif message.text == 'LTC':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/ltc_usd')
                    response = req.json()
                    prc = response['ltc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nLitecoin[LTC] price: ${prc}')
                elif message.text == 'LINK':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/link_usd')
                    response = req.json()
                    prc = response['link_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nChainlink[LINK] price: ${prc}')
                elif message.text == 'TRX':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/trx_usd')
                    response = req.json()
                    prc = response['trx_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nTron[TRX] price: ${prc}')
                elif message.text == 'MANA':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/mana_usd')
                    response = req.json()
                    prc = response['mana_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nDecentraland[MANA] price: ${prc}')
        
        
        elif call.data == 'ru':
            l = 'ru'
            buttons()
            bot.send_message(call.message.chat.id, 'Выберите монету', reply_markup = markup2)

            @bot.message_handler(content_types=['text'])
            def callback1(message):
                if message.text == 'BTC':
                    req = requests.get(f'https://yobit.net/api/3/ticker/btc_usd')
                    response = req.json()
                    prc = response['btc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимость Bitcoin[BTC]: ${prc}')
                elif message.text == 'ETH':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/eth_usd')
                    response = req.json()
                    prc = response['eth_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимость Ethereum[ETH]: ${prc}')
                elif message.text == 'BNB':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/bnbbsc_usd')
                    response = req.json()
                    prc = response['bnbbsc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть BNB[BNB]: ${prc}')
                elif message.text == 'XRP':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/xrp_usd')
                    response = req.json()
                    prc = response['xrp_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть XRP[XRP]: ${prc}')
                elif message.text == 'DOGE':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/doge_usd')
                    response = req.json()
                    prc = response['doge_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Dogecoin[DOGE]: ${prc}')
                elif message.text == 'MATIC':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/matic_usd')
                    response = req.json()
                    prc = response['matic_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Polygon[MATIC]: ${prc}')
                elif message.text == 'LTC':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/ltc_usd')
                    response = req.json()
                    prc = response['ltc_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Litecoin[LTC]: ${prc}')
                elif message.text == 'LINK':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/link_usd')
                    response = req.json()
                    prc = response['link_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Chainlink[LINK]: ${prc}')
                elif message.text == 'TRX':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/trx_usd')
                    response = req.json()
                    prc = response['trx_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Tron[TRX]: ${prc}')
                elif message.text == 'MANA':   
                    req = requests.get(f'https://yobit.net/api/3/ticker/mana_usd')
                    response = req.json()
                    prc = response['mana_usd']['buy']
                    bot.send_message(message.chat.id, f'{datetime.now().strftime("%d.%m.%Y %H:%M")}\nСтоимоть Decentraland[MANA]: ${prc}')

    bot.polling(none_stop=True)


if __name__ == '__main__':
    TELEGRAM_BOT(token)