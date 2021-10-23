from flask import render_template, Blueprint, current_app
from webapp.news.models import News
from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    return render_template('news/index.html',
                           news_list=News.query.order_by(News.published.desc()).all(),
                           page_title='Новости Python',
                           weather=weather_by_city(current_app.config['WEATHER_DEFAULT_CITY']),
                           city=current_app.config['WEATHER_DEFAULT_CITY'].split(',')[0])
