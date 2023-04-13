import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#about: в строке браузера - узнать инфу о юзерагентах
options = Options() #Добавляем опции 
# options.headless = True # Указываем в опциях, что бы браузер не открывался с графической оболочкой (Олдовый метод)
options.add_argument('--headless')# Так удобнее - добавить аргумент: что бы браузер открывался без графической оболочки
options.add_argument("user-agent=Mozilla/5.0") # (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166") - Сохраню в комментах название юзер агентов
driver = webdriver.Chrome(options=options)#Добавляем в наш Хром установленные ранее опции
driver.get("https://plarium.com/en/resource/generator/nickname-generator/")

count = 0 # Создаем каунтер для того, что бы в будущем при достижении определенного количества сделать 'break'
while True: # Цикл while пока тру будем продолжать
    count += 1 # Каждый цикл мы добавляем в каунтер +1
    button_xpath = "//button[text()='Generate']" #Создаем переменную с ХПАФ и вставялем в будущем (Аналог Variables в роботе)
    driver.find_element(By.XPATH, button_xpath).click()
    time.sleep(3)

    name = driver.find_element(By.XPATH, "//input[@name='nickname']").get_attribute("value") #Ищем элемент по ХПАФ и получаем атрибут 'value'
    print(f'Name : {name}')  # синтаксис для добавления переменных в строки/В данном случае мы добавляем ссылаемся на name

    if count == 3:
        a = driver.execute_script("return navigator.userAgent")# Скрип для определения юзер агента . Далее его выведем в консоли
        print("User agent:")
        print(a)
        break #При достижении 3 мы выходим из цикла с помощью синтаксического сахара