from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    first_line = '<h1>hello !</h1>'
    user_agent = request.headers.get('User-Agent')
    #print('request header %s' % request.headers)
    content = first_line + user_agent
    return content

@app.route('/user/<name>')
def user(name):
    return '<h1> hello %s' % name

def index_with_url():
    return '<h1> This is bined by add_url_rule'

app.add_url_rule('/index_with_url/', 'index_with_url', index_with_url)

if __name__ == '__main__':
    app.run(debug=True,threaded=True)


