import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("C:/Users/Monster/Desktop/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com")
arama = driver.find_element(By.NAME,"search_query")
arama.send_keys("NAZAR")
driver.find_element(By.NAME,"Ara").click()




time.sleep(50)
