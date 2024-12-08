import json
from bs4 import BeautifulSoup as bs #сокращеннно юзаем библиотеку
import requests
import json

url = 'https://quotes.toscrape.com/page/1/'
page = requests.get(url)
datajson = "data.json"
indexhtml = "index.html"

citati = []
avtori = []
citati_avtori = [] #Список для записи в джсон 

soup = bs(page.text, "html.parser")
citati2 = soup.findAll('span', class_='text')
avtori2 = soup.findAll('small', class_='author')

for news_item in citati2:
    citati.append(news_item.text) #Кидаем в списки
for news_item in avtori2:
    avtori.append(news_item.text) #Кидаем в списки
for i in range(len(citati)):    
    print(f"{i + 1}) Quete: {citati[i]}, Author: by {avtori[i]}") #Выводим 2 задание

with open(datajson, "w+", encoding='utf-8') as file:
    for i in range(len(citati)):
        p = {'Quote': citati[i], 'Author': avtori[i]}
        citati_avtori.append(p)
    json.dump(citati_avtori, file, indent=5, ensure_ascii=False)

with open(indexhtml, "w+", encoding='utf-8') as file:
    file.write('<html><head><title>Цитаты</title><style>td, th {border:solid 3px green}</style></head>\n')
    file.write('<body style="background-color: rgb(30, 102, 78)">\n')
    file.write('<h1><p align="center"><strong>Великие цитаты</strong></p></h1>\n')
    file.write('<table style = "border:solid 3px green; background-color:yellow">\n')
    file.write('<tr><th>Цитата</th><th>Автор</th></tr>\n')
    for i in range(len(citati)):
        file.write('<tr><td>' + citati[i] + '</td><td>' + avtori[i] + '</td></tr>\n')
    file.write('</table>\n')
    file.write('<h2><a href = "https://quotes.toscrape.com/">Оригинальный источник(Кликабельно)</a></h2>\n')
    file.write('</body></html>\n')
