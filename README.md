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
