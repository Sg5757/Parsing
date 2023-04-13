import requests
from bs4 import BeautifulSoup

# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
 
# headers = {  # Добавил асепт и юзер агент, что бы показать сайту, что мы не бот
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0"
# }
# req = requests.get(url, headers=headers) #получаем заголовок и код страницы
# src = req.text # Получаем текст
# # print(src)

# with open("index.html", "w") as file: # Записываем и создаем файл индекс, 
#     file.write(src) # Записываем туда содержимое переменной src
# ТЕПЕРЬ, КОГДА МЫ СОХРАНИЛИ ХТМЛ ФАЙЛ, МЫ МОЖЕМ ПАРСИТЬ ЕГО БЕЗ ЗАХОДА НА САЙТ = НА ЭТОМ МОМЕНТЕ Я ЗАКОМИТИЛ КОД

with open("index.html") as file:
    src = file.read() # читаем файл, который мы сохранили ранее

soup = BeautifulSoup(src, "lxml") # Добавляем бс и парсен LXML
all_products = soup.find_all(class_="mzr-tc-group-item-href") # Создаем переменную и добавляем туда все данные с указанным классом

for item in all_products:
    item_text = item.text
    item_href = item.get("href")
    print(f"{item_text}: {item_href}")
