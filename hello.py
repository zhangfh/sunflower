from flask import Flask, render_template, session, redirect, url_for,flash
from flask import request
from flask import g
from flask import make_response
from flask import abort
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

mysql_password = os.getenv('FLASK_MYSQL_PASSWORD') or 'default'
mysql_url = 'mysql://root:' + mysql_password + '@localhost/sunflower'
app.config['SECRET_KEY'] = 'wSR03'
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
        
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role')
    
    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64),unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
 
    def __repr__(self):
        return '<User %r>' % self.username

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

@app.route('/getform2',methods=['GET','POST'])
#version 2
def getform2():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('getform2'))
    return render_template('form.html',form=form,name=session.get('name'))

@app.route('/getform3',methods=['GET','POST'])
#version 3
def getform3():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
           flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('getform3'))
    return render_template('form.html',form=form,name=session.get('name'))

@app.route('/getform4',methods=['GET','POST'])
def getform4():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('getform4'))

    return render_template('form4.html',form = form, name = session.get('name'), known = session.get('known', False))

def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)

manager.add_command("shell",Shell(make_context=make_shell_context))

if __name__ == '__main__':
    #app.run(debug=True,threaded=True)
    manager.run()


