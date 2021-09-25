from flask import Flask, render_template
from weather import weather_by_city
from python_org_news import get_news

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', news_list=get_news(), page_title='Новости Python',
                           weather=weather_by_city('Samara,Russia'))


if __name__ == '__main__':
    app.run(debug=True)
