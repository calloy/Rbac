# coding=utf-8
"""
   +----------------------------------------------------------------------
   | application.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_login import LoginManager

import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name=import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        # 加载配置文件
        self.config.from_pyfile('config/base_setting.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'])
        db.init_app(self)


def init_app(app):
    # 注册组件
    register_db(app)
    register_jianjia(app)
    register_error_handle(app)
    register_hooks(app)
    db.init_app(app)
    login_manager.init_app(app)
    template_function_config(app)
    # 创建数据表
    # db.drop_all()
    # db.create_all()


def template_function_config(app):
    """ 模板函数注册 """
    from common.libs.UrlManager import UrlManage
    app.add_template_global(UrlManage.buildStaticUrl, "buildStaticUrl")
    app.add_template_global(UrlManage.buildLibUrl, "buildLibUrl")
    app.add_template_global(UrlManage.buildUrl, "buildUrl")


def register_jianjia(app):
    """ jianjia2 模版 filter，vars,function """
    pass


def register_db(app):
    """数据库db初始化"""
    pass


def register_error_handle(app):
    """注册HTTP错误页面"""

    @app.errorhandler(403)
    def page_403(error):
        return render_template('error/403.html'), 403

    @app.errorhandler(404)
    def page_404(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def page_500(error):
        return render_template('error/500.html'), 500


def register_hooks(app):
    """注册钩子"""
    pass


"""
加载配置文件，初始化插件，程序工程函数
"""
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # 安全等级 None ,basic strong
login_manager.login_view = 'admin.user_login'  # 登陆入口

app = Application(__name__, template_folder=os.getcwd() + '/web/templates/', root_path=os.getcwd())

manager = Manager(app)
init_app(app)
