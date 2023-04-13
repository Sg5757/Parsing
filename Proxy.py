import time
from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_argument("--proxy-server=45.136.58.22:8888") # Заходим на "https://free-proxy-list.net/" и копируем в наш скрипт работающее прокси
driver = webdriver.Chrome(options=option)#Запускаем наш браузер с указанными ранее опциями
driver.get('https://icanhazip.com/')# На этом сайте мы смотрим наш ИП = зашло - ок, не зашло - меняем прокси
ip = driver.find_element(By.XPATH, "//pre[@style='word-wrap: break-word; white-space: pre-wrap;']").text #ПАРСИМ ТЕКСТ!!!! Хоть где-то без скоб
print(f"Наш IP: {ip}") #Добавляем форматирование, что позволит ссылаться на переменные
time.sleep(5)