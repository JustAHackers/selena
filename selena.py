from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from multiprocessing.pool import ThreadPool
import time
pl = []
prolist = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text
prolist1 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all").text
prolist2 = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all").text
dl = []
for i in prolist.splitlines():
    pl.append(i)

for i in prolist1.splitlines():
    pl.append(i)

for i in prolist2.splitlines():
    pl.append(i)
my_url = "https://www.youtube.com/watch?v=Az-SIHZhzgc&list=PLZzMHROnvDL_qhylK7TOLgbRSc7ROwwAO&index=1"

def tri(i):
   try:
    if requests.get(my_url,proxies={"https":"https://"+i},timeout=0.4).status_code == 200:
       print (i)
       tro(i)
   except:
    pass


def fres(i):
    i.refresh()
    i.minimize_window()


def tro(i):
            chrome_options = Options()
            chrome_options.add_argument("--proxy-server="+i)    
            driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
            driver.get("https://youtube.com/c/rezondegrowtopia")
            driver.get(my_url)
            dl.append(driver)

tp = ThreadPool(5000)
tp.map(tri,pl)

tp = ThreadPool(300)
tp.map(fres,dl)


print ("Job Done")
