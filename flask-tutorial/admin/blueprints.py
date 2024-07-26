from flask import Blueprint,render_template

blueprints = Blueprint('blueprints',__name__, static_folder='static',template_folder='templates')

@blueprints.route('/home')
@blueprints.route('/')
def home():
  return render_template('base.html')

@blueprints.route('/test')
def test():
  return '<h1>Testing,Testing</h1>'