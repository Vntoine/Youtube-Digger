import time
import random
from bs4 import BeautifulSoup
import requests
import exrex
import concurrent.futures

def dig_old(code : str):
    res = str(BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code,timeout=3).content,'html.parser').find('title'))
    if res != "<title> - YouTube</title>":
        return "Trouvé : "+res+" -----> "+code

def dig_new(code : str):
    res = requests.get('https://img.youtube.com/vi/'+code+'/1.jpg',timeout=3).status_code
    return "Trouvé -----> "+code if res == 200 else None

def exrexRandom() -> str :
    return ''.join(exrex.getone('[A-Za-z0-9_\-]') for loop in range(11))

def manualRandom() -> str :
    symbols = [chr(i) for i in range(97,123)]
    symbols += [chr(i) for i in range(65,91)]
    symbols += [str(i) for i in range(10)]
    symbols.append('-')
    symbols.append('_')
    return ''.join(symbols[random.randint(0,len(symbols)-1)] for i in range(11))

def code_sample():
    codes = [
        'rqqgKusVLzc','r3qgKusVLzc','rqqgKYsVLzc','rqqgKu7VLz1','e-qgKusVLzc',
        'h5T2X2x7RFU','h4T2X2x7RFU','h4T2X3x7fFU','h4T2X2x74FU','h4T2X2x7-FU',
        manualRandom(),manualRandom(),manualRandom(),manualRandom(),manualRandom(),
        '0HWmhZNG_oc','0HWm4ZNG_oc','0H-mhZNG_oc','AHWmhZNG_oc','0HW41ZNG_oc',
        'd2nmD92YJ44','d2nCP92YJ43','d2nCP92Yh44','d2nCP93YJ44','d2-CP92YJ44',
        manualRandom(),manualRandom(),manualRandom(),manualRandom(),manualRandom()
    ]
    return codes[random.randint(0,len(codes)-1)]

tentatives = 20
time_start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    futures = []
    for i in range(tentatives):
        code = code_sample()
        futures.append(executor.submit(dig_new,code))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())

print('\nOVER ⛏️  :',str(time.time()-time_start)[:4],"secondes\n")