from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0e575292378a0ca28abc0f97df278444'

articles = [
    {
        "id": 1,
        "author": "Andrew Maclean",
        "title": "Article One",
        "body": "What a wonderful man Enzo Ferrari was. He created a brand of cars."
    }, {
        "id": 2,
        "author": "John Doe",
        "title": "Article Two",
        "body": "What a terrible man Henry Ford was. He created an assembly line that made unappealing cars."
    }
]


@app.route('/')
@app.route('/home')
def dispHome():
	return render_template('home.html')

@app.route('/intro')
def dispIntro():
	return render_template('intro.html', title="Intro")

@app.route('/articles')
def dispArticles():
	return render_template('articles.html', articles=articles, title="Articles")

@app.route('/register')
def dispRegister():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def dispLogin():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
