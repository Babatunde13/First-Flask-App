from flask import Flask, render_template

app = Flask(__name__)
posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'Blog Post',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Babatunde Koiki',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	},
	{
		'author': 'Sodiq Agunbiade',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'April 22, 2018'
	},
	{
		'author': 'Sodiq Akinjobi',
		'title': 'Blog Post 4',
		'content': 'Fourth post content',
		'date_posted': 'April 23, 2018'
	}
]

@app.route('/')
def hello():
	return '<h1>Hello world!</h1>'

@app.route('/about')
def about():
	return render_template('about.html', posts=posts, title='About Page')

@app.route('/login')
def login():
	return render_template('login.html', title='Login Page')

@app.route('/signup')
def signup():
	return render_template('signup.html', title='SignUp Page')


if __name__ == '__main__':
	app.run(port=5001, debug=True)
