from flask import Flask,render_template
from admin.blueprints import blueprints

app = Flask(__name__)
app.register_blueprint(blueprints,url_prefix='/admin')

@app.route('/')
def test():
    return '<h1>Testing,Testing</h1>'

if __name__ == '__main__':
    app.run(debug=True,port=2000)

