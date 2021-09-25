import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_python_news(html):
    soup = BeautifulSoup(html, 'html.parser')
    news_list = soup.find('ul', class_='list-recent-posts').findAll("li")
    result_news = []
    for news in news_list:
        title = news.find('a').text
        url = news.find('a')['href']
        published = news.find('time').text
        result_news.append({
            "title": title,
            "url": url,
            "published": published,
        })
    return result_news


def get_news(url="https://www.python.org/blogs/"):
    html = get_html(url)
    if html:
        news = get_python_news(html)
        return news
    return False


if __name__ == '__main__':
    pass
