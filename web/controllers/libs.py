# coding=utf-8
"""
   +----------------------------------------------------------------------
   | libs.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""
from flask import Blueprint, send_from_directory
from application import app


route_lib = Blueprint('lib_page', __name__)


@route_lib.route('/<path:filename>')
def lib(filename):
    return send_from_directory(app.root_path + '/web/lib/', filename)