from flask import Flask, url_for
from flask import render_template as render

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)