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
timeLoopAlert = float(config['time']['time_loop_alertsignal'])


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

    txt = f'{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}\n------'
    #print(txt)
    #messenger.sendtext(f'\n-----------------\nLast Price\n-----------------\n{mycoin1_Price}\n{mycoin2_Price}\n{mycoin3_Price}\n{mycoin4_Price}\n{mycoin5_Price}')


#checkerprice() #check last price ต้อง check เสมอ 
#print(txt) ข้อความส่งอัพเดท last price ไลน์
#print(pc1,pc2,pc3,pc4,pc5) last price ของแต่ละ coin 1 - 5 

mycoin1_str = ''.join(mycoin1) ### เปลี่ยน list เป็น str 
mycoin2_str = ''.join(mycoin2)
mycoin3_str = ''.join(mycoin3)
mycoin4_str = ''.join(mycoin4)
mycoin5_str = ''.join(mycoin5)

condition = (config['alert']['condition'])
import ast
c1 = ast.literal_eval(condition)
#print(c1)
#print(c1['BTCUSDT']['buy'])
#print(type(c1))
#print('----------')

text = ''
def CheckCondition(coin,price):    
    # coin= 'BTCETH', price = 1050000
    global text
    text = ''
    check_buy = c1[coin]['buy']
    if price <= check_buy and price >= check_buy-(check_buy*0.001):
        txt = (f'{Fore.LIGHTRED_EX} \n-----------------\n{coin} ราคาลงแล้ว \nล่าสุดเหลือ: {price:,.3f} รีบซื้อด่วน!\n(ราคาที่อยากได้: {check_buy:,.3f})'.format(coin,price,check_buy))
        #print(txt)
        messenger.sendtext(txt)
        text += txt + '\n'

    check_sell = c1[coin]['sell']
    if price >= check_sell and price <= check_sell+(check_sell*0.001) :
        txt = (f'{Fore.GREEN} \n-----------------\n{coin} ราคาขึ้นแล้ว \nล่าสุดเป็น: {price:,.3f} รีบขายด่วน!\n(ราคาที่อยากขาย: {check_sell:,.3f})'.format(coin,price,check_sell))
        #print(txt)
        messenger.sendtext(txt)
        text += txt + '\n'
    
    else:
        print(f'{Fore.LIGHTCYAN_EX}wait signal . . .')



#checkerprice()
print(txt)
def CheckConditionAll():
    CheckCondition(mycoin1_str,pc1)
    print(text)
    CheckCondition(mycoin2_str,pc2)
    print(text)
    CheckCondition(mycoin3_str,pc3)
    print(text)
    CheckCondition(mycoin4_str,pc4)
    print(text)
    CheckCondition(mycoin5_str,pc5)
    print(text)
    #time.sleep(timeLoopAlert)

#CheckConditionAll()

alertsignal = (config['notify']['alertsignal'])

welcome =  '-------------------------------------------'
welcome2 = '----- Welcome to CheckerBinance Bot -------'
welcome3 = 'Signal Alert mode : on '
welcome4 = f'Line Notify Alert : {alertsignal}'
welcome5 = '-------------- Signal Alert ---------------'
print(f'{Fore.LIGHTWHITE_EX}{welcome}\n{welcome2}\n{welcome3}\n{welcome4}\n{welcome5}')
while True:
    if alertsignal == 'on' :
        checkerprice()
        CheckConditionAll()
    elif alertsignal == 'off' :
        checkerprice()
    time.sleep(timeLoopAlert)


