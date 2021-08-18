# CheckerBinance.py
from binance.client import Client
from songline import Sendline

api_key = ''
api_secret = ''
client = Client(api_key, api_secret)
token = ''
messenger = Sendline(token)

import time
timeLoop = []

mycoin1 = ''
mycoin2 = ''
mycoin3 = ''
mycoin4 = ''
mycoin5 = ''

while True:
    prices = client.get_all_tickers() #request ใหม่ทุกครั้ง
    mycoin1_Price = []
    mycoin2_Price = []
    mycoin3_Price = []
    mycoin4_Price = []
    mycoin5_Price = []

    for p in prices:
        for c in mycoin1:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin1_Price = ('{} : {:,.3f} USDT'.format(sym, pc))

    for p in prices:
        for c in mycoin2:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin2_Price = ('{} : {:,.3f} USDT'.format(sym, pc))

    for p in prices:
        for c in mycoin3:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin3_Price = ('{} : {:,.3f} USDT'.format(sym, pc))
    for p in prices:
        for c in mycoin4:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin4_Price = ('{} : {:,.3f} USDT'.format(sym, pc))

    for p in prices:
        for c in mycoin5:
            sym = c
            if p['symbol'] == sym:
                #print(p)
                pc = float(p['price']) #ราคาบิทคอยหน่อย USDT
                mycoin5_Price = ('{} : {:,.3f} USDT'.format(sym, pc))

    print(f'{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}\n------')
    messenger.sendtext(f'\n-----------------\nLast Price\n-----------------\n{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}')

    time.sleep(timeLoop)
