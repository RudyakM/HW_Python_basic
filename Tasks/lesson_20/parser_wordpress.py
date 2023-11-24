import requests
from bs4 import BeautifulSoup


url = 'https://wordpress.org/plugins/'
r = requests.get(url)


if r.status_code == 200:
    soup = BeautifulSoup(r.text, 'html.parser')
    sections = soup.find_all('section')

    for data in sections:
        categories = data.find('h2').text.strip('\n')
        print(f'\n{categories}:')
        articles = data.find_all('article')
        for article in articles:
            rating = article.find('span', class_="rating-count")
            stars = article.find('div', class_="wporg-ratings")
            print(article.find("header").text.strip('\n'), '===> ', stars.get_attribute_list('aria-label'), rating.find('a').text)
