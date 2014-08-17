from flask import Flask, render_template
from flask.ext.script import Manager


# create application instance
# web server passes all request to this object using WSGI
# __name__ used to determine root path of app so that it can later
# find resource files relative to location of app
app = Flask(__name__)
manager = Manager(app)


# view functions
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# used to ensure dev server only started when app is
# executed directly
# change this for production
if __name__ == '__main__':
    manager.run()
