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

