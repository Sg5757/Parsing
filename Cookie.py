import time
import pickle
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
login = 'standard_user'
password = 'secret_sauce'
driver.get("https://www.saucedemo.com/")

# driver.find_element(By.ID, 'user-name').send_keys(login)     #ДЕЛАЕМ ЭИ ШАГИ ДЛЯ СОХРАНЕНИЯ КУКИ
# driver.find_element(By.ID, 'password').send_keys(password)
# driver.find_element(By.NAME, 'login-button').click()
# time.sleep(3)
# pickle.dump(driver.get_cookies(), open('session', 'wb')) #Сохраняем куки в файл "session"

for cookie in pickle.load(open('session', 'rb')):
    driver.add_cookie(cookie)
time.sleep(3)
print('Cookie saved')
driver.refresh()

