from flask import Flask, render_template
from flask import request
from flask import g
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


app.config['SECRET_KEY'] = 'wSR03'


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
        
@app.before_request
def helloworld():
    print("helloworld will be called every url access")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/')
def index():
    datetime_now = datetime.utcnow()
    return render_template('index.html', current_time=datetime_now)

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

@app.route('/link')
def get_link():
    return render_template('link.html')

@app.route('/getform',methods=['GET','POST'])
#version 1
def getform():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('form.html',form=form,name=name)


if __name__ == '__main__':
    #app.run(debug=True,threaded=True)
    manager.run()


