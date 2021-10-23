import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.news.models import News
from webapp.db import db

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_news(url="https://www.python.org/blogs/"):
    html = get_html(url)
    if html:

        soup = BeautifulSoup(html, 'html.parser')
        news_list = soup.find('ul', class_='list-recent-posts').findAll("li")
        for news in news_list:

            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time')

            try:
                published = datetime.strptime(published['datetime'], '%Y-%m-%d')
            except(ValueError):
                published = datetime.now()

            save_news(title=title, url=url, published=published)

    return False


if __name__ == '__main__':
    pass
