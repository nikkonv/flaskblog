
from flask import url_for, flash, redirect, request
from flask import render_template as render
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


post = [
    {
        'author': 'Nicolas',
        'content': 'Hello'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render('home.html', posts=post)

@app.route('/about')
def about():
    return render('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login.', 'success')
        return redirect(url_for('home'))
    return render('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('account')) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render('account.html', title='Account')