# coding=utf-8
"""
   +----------------------------------------------------------------------
   | www.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""
from application import app
from web.controllers.libs import route_lib
from web.controllers.static import route_static
from web.controllers.user.user import route_user

app.register_blueprint(route_static, url_prefix='/static')
app.register_blueprint(route_lib, url_prefix="/lib")

app.register_blueprint(route_user, url_prefix='/user')

