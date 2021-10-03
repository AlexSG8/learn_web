from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news
from webapp.model import db, News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():

        return render_template('index.html',
                               news_list=News.query.order_by(News.published.desc()).all(),
                               page_title='Новости Python',
                               weather=weather_by_city(app.config['WEATHER_DEFAULT_CITY']),
                               city=app.config['WEATHER_DEFAULT_CITY'].split(',')[0])
    return app
