from flask import Flask,request,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',content='Testing')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user',user=user))
    else:
        return render_template('login.html')

@app.route('/<user>')
def user(user):
    return f'<h1>{user}</h1>'

if __name__ == '__main__':
    app.run(debug=True,port=2000)