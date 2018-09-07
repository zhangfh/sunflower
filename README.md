Flask framework
1. tag: 2a
   python hello.py
   access:  127.0.0.1:5000 ,  127.0.0.1:5000/user/li
2. tag: 2b
   use request
   enable multi thread
3. tag: 2c
   1)use current_app by python shell   

   ##################################
   use python shell to use current_app
   (venv)python
   >>> from hello import app
   >>> from flask import current_app
   >>> current_app
   <LocalProxy unbound>
   >>> app_ctx = app.app_context()
   >>> app_ctx.push()
   >>> current_app.name
   >>> app_ctx.pop()

   2)use add_url_rule() to define route
   3)check url route map with python shell
   (venv)python
   >>>from hello import app
   >>>app.url_map

4. tag : 2d
   1) g 处理请求时用作临时存储的对象，每次请求都会重设这个变量
   127.0.0.1:5000/user/123
   2) hook
      before_first_request
      before_request
      after_request
      teardown_request
      see sample code: helloword(hello.py)

   3) response
      400 request invalid (see indexerror)
      make_response(see makeresponse)
   4) redirect
      see redirectbaidu
   5) abort
      see makeabort
5. tag 2e
   flask-script
   1) python hello.py runserver
   2) python hello.py runserver -h 0.0.0.0  (allow any computer access your web server)
   3) python hello.py shell
      >>> from hello import app
      >>> from hello import manager

6. tag 3a
   render_template
   python hello.py runserver -h 0.0.0.0
   http://192.168.0.107:5000/
   http://192.168.0.107:5000/user/zhang3f
7. tag 3b
   use bootstrap template
   http://192.168.0.107:5000/user/zhang3f
8. tag 3e
   use own javascript file
9. tag 3f
   template/base.html  base template
   template/user.html  use base.html as parent template
   template/404.html , template/500.html as errorhandler
10. tag 3g
   url_for      127.0.0.1:5000/link
11. tag 3h
    static for favicon
12. tag 3i
    use datetime to get time
    use moment to format time in browser
    index.html(base.html include moment.js)
13. tag 4a
    use form    127.0.0.1:5000/getform
14. tag 4b
    form(post--redirect--get) 127.0.0.1:5000/getform2
15. tag 4c
    flash 127.0.0.1:5000/getform3

16. tag 5a
    1). export FLASK_MYSQL_PASSWORD in venv/bin/activate
    2). set mysql uri
    3). mysql database: sunflower
	CREATE DATABASE IF NOT EXISTS sunflower DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
    4). pip install mysql-python 
    
    5) use python shell
       >>> from hello import db
       >>> db.create_all()
       use mysql to view:
       mysql >> use sunflower
       mysql >> show tables;
       mysql >> desc users;

    6) use mysql in view  127.0.0.1:5000/getform4
17. tag 5b
    import shell for convinence
18. tag 5c
    migration shell command
    >>> python hello.py db init
    >>> python hello.py db migrate -m "initial migration"
    >>> python hello.py db upgrade

19. tag 6a 
    1) add config in venv/bin/activate
       FLASK_MAIL_USERNAME
       FLASK_MAIL_PASSWORD
       FLASK_MAIL_SENDER
    2) use python to send email
	>>> from flask_mail import Message
	>>> from hello import mail
	>>> msg = Message('test subject today', sender='xxx@163.com',recipients=['xxx@163.com'])
	>>> msg.body = 'text body'
	>>> msg.html = '<b>This is from python Shell</b>'
	>>> with app.app_context():
	...     mail.send(msg)
    3) send email with template both sync and async
20. tag 7a
    1) tree -I 'venv|migrations|*.pyc' 
	.
	├── app
	│   ├── email.py
	│   ├── __init__.py
	│   ├── main
	│   │   ├── errors.py
	│   │   ├── forms.py
	│   │   ├── __init__.py
	│   │   └── views.py
	│   ├── models.py
	│   ├── static
	│   │   └── favicon.ico
	│   └── templates
	│       ├── 404.html
	│       ├── 500.html
	│       ├── base.html
	│       ├── index.html
	│       └── mail
	│           ├── new_user.html
	│           └── new_user.txt
	├── config.py
	├── manage.py
	├── README.md
	└── requirements.txt


21. tag 8a
    unit test
    python manage.py test
    test/__init__.py test/test_basics.py  test/test_user_model.py
22. tag 8b
    auth blueprint and route: http://192.168.0.107:5000/auth/login
23. tag 8c
    login
    #python manage.py  db migrate -m "v0.3"
    #python manage.py db upgrade
    email : john@163.com password: cat 
