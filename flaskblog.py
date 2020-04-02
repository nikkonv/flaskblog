from flask import Flask, url_for
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
    return render('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)