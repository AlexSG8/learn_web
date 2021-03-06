from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from webapp.user.forms import LoginForm
from webapp.user.models import User
from flask_login import login_user, logout_user, current_user
from webapp.weather import weather_by_city

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('user/login.html',
                           page_title=title,
                           form=login_form,
                           weather=weather_by_city(current_app.config['WEATHER_DEFAULT_CITY']),
                           city=current_app.config['WEATHER_DEFAULT_CITY'].split(',')[0])


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Вы вошли на сайт, {user.username}')
            return redirect(url_for('news.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились.')
    return redirect(url_for('news.index'))
