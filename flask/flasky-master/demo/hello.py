from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)

from flask.ext.script import Manager
manager = Manager(app)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
# ...
if __name__ == '__main__':
    manager.run()


