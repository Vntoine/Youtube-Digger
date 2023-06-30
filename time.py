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

tentatives = 1000
time_start = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(tentatives):
        futures.append(executor.submit(dig_new,manualRandom()))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())

print('\nOVER ⛏️  :',str(time.time()-time_start)[:4],"secondes\n")