import datetime
import time

from pytube import YouTube

from flask import Flask, render_template, session, make_response, jsonify, url_for, request
from flask_login import LoginManager, logout_user, login_required
from werkzeug.utils import redirect

from data import db_session
from data.downloadform import DownloadForm
from data.loginform import LoginForm
from data.registerform import RegisterForm
from data.users import User

from static.python.style import base_style, login_style, register_style

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hfu bs8f9vuronr 6tb14 021rtetoehn02br86lwo;'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

login_manager = LoginManager()
login_manager.init_app(app)

T = 1


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    global T
    T += 1
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, web_style=login_style(T))
    return render_template('login.html', title='Авторизация', form=form, web_style=login_style(T))


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    global T
    T += 1
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают", web_style=register_style())
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть", web_style=register_style())
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form, web_style=register_style())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init('db/blogs.db')
    app.run()


@app.route('/', methods=['POST', "GET"])
def home():
    global T
    T += 1
    form = DownloadForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            address = form.address.data
            try:
                video = YouTube(address)
                print(video.title)
            except:
                print('Неправильная ссылка')
    return render_template("download.html", form=form, style=base_style(T)[0])


@app.route('/session_test')
def session_test():
    visits_count = session.get('visits_count', 0)
    session['visits_count'] = visits_count + 1
    return make_response(f'Ты посетил страницу {visits_count + 1} раз')


if __name__ == '__main__':
    main()