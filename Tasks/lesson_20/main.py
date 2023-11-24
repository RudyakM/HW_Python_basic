import requests
from bs4 import BeautifulSoup


url = 'https://mignews.com'
page = requests.get(url)
print(page.status_code)

all_news = []
filtered_news = []
news = []
time = []

soup = BeautifulSoup(page.text, 'html.parser')
all_news = soup.findAll('article', class_="post mb-2")

# Отфильтровал новости, будут показываться только важные(красные) новости из сайта
for data in all_news:
    if data.find('div', class_="btn btn-primary btn-xs rounded-0"):
        filtered_news.append(data)

# Из списка filtered_news взял время написания новости и поместил в нововый список time
for data in filtered_news:
    time.append(data.find('div', class_="btn btn-primary btn-xs rounded-0").text.strip('\n'))

# Из списка filtered_news взял текст новости и поместил в нововый список news
for data in filtered_news:
    news.append(data.find('div', class_="text-color-dark").text.strip('\n'))

# Обьеденил елементы time и news, поместил их в список time_news и вывел результат 
time_news = list(map(lambda x, y: x + ' ' + y, time, news))
for data in time_news:
    print(data)
