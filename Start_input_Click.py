import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window() #НЕ ЗАБЫВАЙ СКОБКИ!!! везде
driver.get('https://www.saucedemo.com/')
html = driver.find_element(By.TAG_NAME, "html") #Создаем переменную для отправки KEYS из библиотек
driver.find_element(By.ID, 'user-name').send_keys("standard_user") #Ищем элемент с помощью библиотeки BY, далее отправляем в это поле наш логин
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click() #Находим элемент кнопки с помощью BY и применяем клик () [не забывай про скобки кргулые]

for i in range(10): #создадим цикл для того что бы в нем нажать кнопку с помобю кейс кнопку вниз 10 раз
    time.sleep(1)
    html.send_keys(Keys.DOWN)
time.sleep(3)

block_backpages = driver.find_element(By.CLASS_NAME, "inventory_list") #Обозначаем блок в переменную для того, что бы в будущем выбирать из него элементы
backpages = block_backpages.find_elements(By.CLASS_NAME, "inventory_item") #Вот тут и выбираем элементы
for back in backpages:
    print(back.get_attribute('class')) #Элементарный цикл,  для отображения атрибутов 
