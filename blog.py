from flask import Flask


# create application instance
# web server passes all request to this object using WSGI
# __name__ used to determine root path of app so that it can later
# find resource files relative to location of app
app = Flask(__name__)


# view functions
@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,  %s!</h1>' % name


# used to ensure dev server only started when app is
# executed directly
# change this for production
if __name__ == '__main__':
    app.run(debug=True)
