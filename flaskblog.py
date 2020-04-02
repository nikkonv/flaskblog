from flask import Flask, url_for, flash, redirect
from flask import render_template as render
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6075aa775d03746e78358597aa23176e1e9c7a2f7125720f91f23250de8ece34'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)