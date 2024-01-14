import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('crawler\proxies.txt', 'r') as f:
    proxies = f.read().split('\n')
    for p in proxies:
        q.put(p)

def check_proxy():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            r = requests.get('http://ipinfo.io/json', proxies={'http': proxy, 'https': proxy})
        except:
            continue
        if r.status_code == 200:
                print(proxy)
                valid_proxies.append(proxy)
for _ in range(10):
    t = threading.Thread(target=check_proxy)
    t.start()
    t.join()
