from flask import Flask, render_template
from flask import request
from flask import g
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


        
@app.before_request
def helloworld():
    print("helloworld will be called every url access")

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/indexerror')
def indexerror():
    return '<h1>Bad Request</h1>', 400


@app.route('/makeresponse')
def indexresponse():
    response = make_response('<h1> This document carries a cooie!</h1>')
    response.set_cookie('answer','65')
    return response

@app.route('/redirectbaidu')
def indexredirect():
    return redirect('http://www.baidu.com')

@app.route('/makeabort')
def indexabort():
    abort(404)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

def index_with_url():
    return '<h1> This is bined by add_url_rule'

app.add_url_rule('/index_with_url/', 'index_with_url', index_with_url)


if __name__ == '__main__':
    #app.run(debug=True,threaded=True)
    manager.run()


