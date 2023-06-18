import requests
from bs4 import BeautifulSoup
import exrex
import concurrent.futures
import time

def dig(code : str):
    res = str(BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code,timeout=3).content,'html.parser').find('title'))
    if res != "<title> - YouTube</title>":
        return "Trouvé : "+res+" -----> "+code

tentatives = 100
thread_start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for i in range(tentatives):
        code = ''.join(exrex.getone('[A-Za-z0-9_\-]') for loop in range(11))
        futures.append(executor.submit(dig,code))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())
print('\nOVER ⛏️  :',str(time.time() - thread_start)[:4],"secondes\n")