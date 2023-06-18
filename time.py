import time
import random
from bs4 import BeautifulSoup
import requests
import exrex

def dig(code : str):
    res = str(BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code,timeout=3).content,'html.parser').find('title'))
    if res != "<title> - YouTube</title>":
        return "Trouvé : "+res+" -----> "+code

time_start = time.time()

symbols = [chr(i) for i in range(97,123)]
symbols += [chr(i) for i in range(65,91)]
symbols += [str(i) for i in range(10)]
symbols.append('-')
symbols.append('_')


# Mettre en commentaire pour tester les solutions
for i in range(1000):
    code = ''.join(exrex.getone('[A-Za-z0-9_\-]') for loop in range(11))
    #code = ''.join(symbols[random.randint(0,len(symbols)-1)] for i in range(11))

print('OVER :',str(time.time()-time_start)[:4],"secondes")