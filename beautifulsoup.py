from bs4 import BeautifulSoup

with open("index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml") #Создаем обьект класса бс и указываем переменную и парсер

title = soup.title # Получаем данные из тэга title
# print(title.text) - выводим текст 
page_1 = soup.find("h1") # Назначаем в переменную данные из тэга Н1
page_all_h1 = soup.find_all("h1")
for item in page_all_h1: # Элеменарно выводим в цикле данные из списка
    
    print(item.text)