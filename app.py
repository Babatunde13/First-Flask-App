from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def hello():
	return '<h1>Hello world!</h1>'

@app.route('/login')
def about():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(port=5001, debug=True)
