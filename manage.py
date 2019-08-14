# coding=utf-8
"""
   +----------------------------------------------------------------------
   | manage.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""
from application import app, manager
from flask_script import Server

# add script
manager.add_command("runserver", Server(host='0.0.0.0', port=5000, use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == "__main__":
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        # 引入一个错误打印模块
        import traceback
        traceback.print_exc()