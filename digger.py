import requests
from bs4 import BeautifulSoup
import random
import concurrent.futures
import time

# Pour un code donné, la fonction teste le titre de la page pour déterminer si elle renvoie vers une vidéo
def dig(code : str):
    res = str(BeautifulSoup(requests.get('https://www.youtube.com/watch?v='+code,timeout=3).content,'html.parser').find('title'))
    if res != "<title> - YouTube</title>":
        return "Trouvé : "+res+" -----> "+code

symbols = [chr(i) for i in range(97,123)]       #   symbols correspond à un tableau semblable à une regex pour générer un code valide,
symbols += [chr(i) for i in range(65,91)]       #        j'utilisais anciennement le module exrex pour générer un caractère
symbols += [str(i) for i in range(10)]          #       aléatoire à partir de la regex [A-Za-z0-9_\-] mais après vérification
symbols.append('-')                             #           elle est moins performante qu'avec la solution ici présente :
symbols.append('_')                             #     sur 10 000 essais, exrex -> 10.6 secondes contre 0.73 secondes maintenant

tentatives = 1000
thread_start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
    futures = []
    for i in range(tentatives):
        code = ''.join(symbols[random.randint(0,len(symbols)-1)] for i in range(11))
        futures.append(executor.submit(dig,code))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())
print('\nOVER ⛏️  :',str(time.time() - thread_start)[:4],"secondes")



#               Récapitulatif des optimisations
#
#   exrex :
#           - sur 10 000 tentatives -> 10.7 secondes (exrex) contre 0.9 secondes (manual)
#           - sur 1 000 tentatives -> 1.09 secondes (exrex) contre 0.09 secondes (manual)
#
#   max_workers :
#       Correspond au nombre de threads alloué au ThreadPoolExecutor
#           - sur 100 tentatives, utilisation d'exrex : 24.26 secondes (anciennement)
#                                                       6.45 secondes avec 5 max_workers
#                                                       4.65 secondes avec 10 max_workers
#           - sur 1 000 : 45.9 secondes (5 max_workers) et 42.47 secondes (10 max_workers)
#             d'où le 7 dans le script actuel, bon compromis entre efficacité et coût (processeur, éviter de trop le solliciter)