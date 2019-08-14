# coding=utf-8
"""
   +----------------------------------------------------------------------
   | static.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""
from flask import Blueprint,send_from_directory
from application import app


route_static = Blueprint('static_page', __name__)


@route_static.route('/<path:filename>')
def static(filename):
    return send_from_directory(app.root_path + '/web/static/', filename)