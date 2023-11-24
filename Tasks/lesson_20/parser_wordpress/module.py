import requests
from bs4 import BeautifulSoup


class ParserWordPress:


    def __init__(self):
        self.bingo = '=' * 50
        self.url = 'https://wordpress.org/plugins/'


    def requester(self):
        r = requests.get(self.url)
        return r
    

    def get_all_data(self, r):
        soup = BeautifulSoup(r.text, 'html.parser')
        sections = soup.find_all('section')
        return sections


    def get_info(self, sections):
        for data in sections:
            category = data.find('h2').text.strip('\n')
            print(f'\n{self.bingo}')
            print(f'Category: {category}')
            print(self.bingo)
            articles = data.find_all('article')
            for article in articles:
                plugin = article.find("header").text.strip('\n')
                rating = article.find('span', class_="rating-count").find('a').text
                stars = article.find('div', class_="wporg-ratings").get_attribute_list('aria-label')
                print(f'Plugin name: {plugin}')
                print(f'Stars: {stars}')
                print(f'Plugin rating: {rating}')
                print(self.bingo)

