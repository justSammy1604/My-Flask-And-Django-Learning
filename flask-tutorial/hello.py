from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f"<h2>Hello {name}<h2>"

@app.route('/admin')
def admin():
    return redirect(url_for('user',name='Admin!!'))

if __name__ == '__main__':
    app.run(debug=True,port=3300)