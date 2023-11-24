import requests
from bs4 import BeautifulSoup


bingo = '=' * 50
url = 'https://wordpress.org/plugins/'
r = requests.get(url)


if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    sections = soup.find_all('section')

    for data in sections:
        category = data.find('h2').text.strip('\n')
        print(f'\n{bingo}')
        print(f'Category: {category}')
        print(bingo)
        articles = data.find_all('article')
        for article in articles:
            plugin = article.find("header").text.strip('\n')
            rating = article.find('span', class_="rating-count").find('a').text
            stars = article.find('div', class_="wporg-ratings").get_attribute_list('aria-label')
            print(f'Plugin name: {plugin}')
            print(f'Stars: {stars}')
            print(f'Plugin rating: {rating}')
            print(bingo)
