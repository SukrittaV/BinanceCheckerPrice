# CheckerBinance.py
from typing import Text
from binance.client import Client
from songline import Sendline
from configparser import ConfigParser
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

file = './configChecker.ini'
config = ConfigParser()
config.read(file)


api_key = (config['account']['api_Binance'])
api_secret = (config['account']['api_secret'])
client = Client(api_key, api_secret)

token = (config['account']['token_Line'])
messenger = Sendline(token)

import time
timeLoop = float(config['time']['time_loop_lastpricecheck'])

mycoin1 = [(config['coin']['mycoin01'])]
mycoin2 = [(config['coin']['mycoin02'])]
mycoin3 = [(config['coin']['mycoin03'])]
mycoin4 = [(config['coin']['mycoin04'])]
mycoin5 = [(config['coin']['mycoin05'])]

#print(type(mycoin1))
#print(str(mycoin1))

pc1 = ''
pc2 = ''
pc3 = ''
pc4 = ''
pc5 = ''

mycoin1_Price = ''
mycoin2_Price = ''
mycoin3_Price = ''
mycoin4_Price = ''
mycoin5_Price = ''

txt = ''

def checkerprice():
    global pc1,pc2,pc3,pc4,pc5,mycoin1_Price,mycoin2_Price,mycoin3_Price,mycoin4_Price,mycoin5_Price,txt
    prices = client.get_all_tickers() #request ใหม่ทุกครั้ง
    txt = ''

    for p in prices:
        for c in mycoin1:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc1 = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin1_Price = ('{} : {:,.3f} USDT'.format(sym, pc1))

    for p in prices:
        for c in mycoin2:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc2 = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin2_Price = ('{} : {:,.3f} USDT'.format(sym, pc2))

    for p in prices:
        for c in mycoin3:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc3 = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin3_Price = ('{} : {:,.3f} USDT'.format(sym, pc3))
    for p in prices:
        for c in mycoin4:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc4 = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin4_Price = ('{} : {:,.3f} USDT'.format(sym, pc4))

    for p in prices:
        for c in mycoin5:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc5 = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin5_Price = ('{} : {:,.3f} USDT'.format(sym, pc5))

    txt = f'{Fore.GREEN}{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}{Fore.LIGHTWHITE_EX}\n-------------------------------------------'
    print(txt)
    #messenger.sendtext(f'\n-----------------\nLast Price\n-----------------\n{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}')


lastpricecheck = (config['notify']['lastpricecheck'])

welcome =  '-------------------------------------------'
welcome2 = '----- Welcome to CheckerBinance Bot -------'
welcome3 = 'Last Price mode : on '
welcome4 = f'Line Notify Alert : {lastpricecheck}'
welcome5 = '--------------- Last Price ----------------'
print(f'{Fore.LIGHTWHITE_EX}{welcome}\n{welcome2}\n{welcome3}\n{welcome4}\n{welcome5}')
while True:
    if lastpricecheck == 'on' :
        checkerprice()
        messenger.sendtext(f'\n-----------------\nLast Price\n-----------------\n{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}')
    elif lastpricecheck == 'off' :
        checkerprice()
    time.sleep(timeLoop)

    
    
    
    