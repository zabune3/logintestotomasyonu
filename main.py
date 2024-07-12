import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service("C:/Users/Monster/Desktop/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.apple.com")
link = driver.current_url
baslik = driver.title
print("Doğru Sayfaya Giriş Yaptınız: " + baslik)
driver.get("https://www.youtube.com")
link1 = driver.current_url
baslik1 = driver.title
print("Doğru Sayfaya Giriş Yaptınız: " + baslik1)












time.sleep(100)