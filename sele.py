from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from multiprocessing.pool import ThreadPool
pl = []
prolist = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text
my_url = "https://www.youtube.com/watch?v=Az-SIHZhzgc&list=PLZzMHROnvDL_qhylK7TOLgbRSc7ROwwAO&index=1"
def tri(i):
   try:
    if requests.get(my_url,proxies={"https":"https://"+i},timeout=1).status_code == 200:
       tro(i)
       print (i)
       time.sleep(1)
   except:
    pass

def tro(i):
            chrome_options = Options()
            chrome_options.add_argument("--proxy-server="+i)    
            driver = webdriver.Chrome("chromedriver.exe",chrome_options=chrome_options)
            driver.get("https://youtube.com/c/rezondegrowtopia")
            driver.get(my_url)
            time.sleep(7)
            driver.minimize_window()

tp = ThreadPool(1000)
tp.map(tri,prolist.splitlines())