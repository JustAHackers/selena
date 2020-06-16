from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from multiprocessing.pool import ThreadPool
prolist = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all").text
my_url = "https://www.youtube.com/playlist?list=PLZzMHROnvDL_qhylK7TOLgbRSc7ROwwAO"
def tro(i):
    try:
     if requests.get(my_url,proxies={"https":"https://"+i}).status_code == 200:
            chrome_options = Options()
            chrome_options.add_argument("--proxy-server="+i)    
            driver = webdriver.Chrome(chrome_options=chrome_options)
            driver.get(my_url)
            tombol = driver.find_elements_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse[3]/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/div[4]/ytd-menu-renderer/div/ytd-button-renderer[1]/a/yt-icon-button/button")
            tombol[0].click()
    except:
       pass
tp = ThreadPool(100)
tp.map(tro,prolist.splitlines())