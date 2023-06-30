import requests
import random
import concurrent.futures
import time

# Pour un code donné, la fonction effectue une requête vers les images associées à la vidéo (thumbnails).
def dig(code : str):
    res = requests.get('https://img.youtube.com/vi/'+code+'/1.jpg',timeout=3).status_code
    return "Trouvé : "+code if res == 200 else None

symbols = [chr(i) for i in range(97,123)]       #   symbols correspond à un tableau semblable à une regex pour générer un code valide,
symbols += [chr(i) for i in range(65,91)]       #        j'utilisais anciennement le module exrex pour générer un caractère
symbols += [str(i) for i in range(10)]          #       aléatoire à partir de la regex [A-Za-z0-9_\-] mais après vérification
symbols.append('-')                             #           elle est moins performante qu'avec la solution ici présente :
symbols.append('_')                             #     sur 10 000 essais, exrex -> 10.6 secondes contre 0.73 secondes maintenant

tentatives = 1000
thread_start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(tentatives):
        code = ''.join(symbols[random.randint(0,len(symbols)-1)] for i in range(11))
        futures.append(executor.submit(dig,code))
    for future in concurrent.futures.as_completed(futures):
        if future.result() is not None:
            print(future.result())

print('\nOVER ⛏️  :',str(time.time() - thread_start)[:5],"secondes\n")



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
#               PS: Mettre une valeur de max_workers est préférable. Dans mon cas, c'est-à-dire avec mon processeur actuel,
#               le ThreadPoolExecutor alloue 20 threads, pour des résultats quasi-égaux qu'avec 10 threads.
#
#   Lien de la requête :
#           - sur 10 requêtes -> 4.26 secondes (https://www.youtube.com/watch?v=............)
#           - sur 10 requêtes -> 1.15 secondes (https://img.youtube.com/vi/.........../1.jpg)
#
#