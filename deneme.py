import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/Monster/Desktop/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)


driver.maximize_window()
driver.get("https://facebook.com") #giris yapılacak site URL
giris = driver.find_element(By.ID,"email") #site ici mail id
giris.send_keys("..............")
sifre = driver.find_element(By.ID,"pass") #site ici sifre id
sifre.send_keys("...............")
driver.find_element(By.NAME,"login").click() #login button id
driver.execute_script("window.scrollBy(0,300)","")




time.sleep(60)



