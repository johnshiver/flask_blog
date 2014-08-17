from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap


# create application instance
# web server passes all request to this object using WSGI
# __name__ used to determine root path of app so that it can later
# find resource files relative to location of app
app = Flask(__name__)
bootstrap = Bootstrap(app)


# view functions
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# used to ensure dev server only started when app is
# executed directly
# change this for production
if __name__ == '__main__':
    app.run()
