import requests
from bs4 import BeautifulSoup
import exrex

tentatives = 1000
tab = [i for i in range(50,1000,50)]

for i in range(tentatives):
    code = ''.join(exrex.getone('[A-Za-z0-9_\-]') for loop in range(11))
    retour = BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code).content,'html.parser')
    res = str(retour.find('title'))
    if res != "<title> - YouTube</title>":
        print("Trouvé : "+res+" -----> "+code)
    if i in tab:
        print('In progress... ',str(i//10)+"%")
