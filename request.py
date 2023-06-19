import requests
import time

start_time = time.time()
for i in range(10):
    res = requests.get('https://img.youtube.com/vi/rqqgKusVLzc/1.jpg',timeout=3).status_code

print(f"Résultat en {time.time()-start_time} secondes")


# 10 requêtes en 4.26 secondes avec le lien "https://www.youtube.com/watch?v="
# 10 requêtes en 1.34 secondes avec le lien "https://img.youtube.com/vi/??????/0.jpg" <- miniature de la vidéo
# 10 requêtes en 1.15 secondes avec le lien "https://img.youtube.com/vi/??????/1.jpg" <- plus petite image