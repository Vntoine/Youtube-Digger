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
    res = str(BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code,timeout=3).content,'html.parser').title.text)
    return "Trouvé : "+res+" -----> "+code if res != " - YouTube" else None

def exrexRandom() -> str :
    return ''.join(exrex.getone('[A-Za-z0-9_\-]') for loop in range(11))

def manualRandom() -> str :
    symbols = [chr(i) for i in range(97,123)]
    symbols += [chr(i) for i in range(65,91)]
    symbols += [str(i) for i in range(10)]
    symbols.append('-')
    symbols.append('_')
    return ''.join(symbols[random.randint(0,len(symbols)-1)] for i in range(11))


tentatives = 100
time_start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    futures = []
    for i in range(tentatives):
        code = manualRandom()
        futures.append(executor.submit(dig_old,code))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())

print('OVER :',str(time.time()-time_start)[:4],"secondes")