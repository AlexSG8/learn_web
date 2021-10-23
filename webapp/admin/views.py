from flask import Blueprint, render_template, current_app
from flask_login import current_user, login_required
from webapp.user.decorators import admin_required
from webapp.weather import weather_by_city

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def admin_index():
    return render_template('admin/dashboard.html',
                           page_title='Новости Python',
                           weather=weather_by_city(current_app.config['WEATHER_DEFAULT_CITY']),
                           city=current_app.config['WEATHER_DEFAULT_CITY'].split(',')[0])