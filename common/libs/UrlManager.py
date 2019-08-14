# coding=utf-8
"""
   +----------------------------------------------------------------------
   | UrlManager.py 
   +----------------------------------------------------------------------
   | Copyright (c) 2019 http://Yooou.cn All rights reserved.
   +----------------------------------------------------------------------
   | Author: calloy<calloy2007@gmail.com>
   +----------------------------------------------------------------------
   | 2019/8/14
   +----------------------------------------------------------------------
"""


class UrlManage(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        ver = "%s" % 201908
        path = "/static" + path + "?Ver=" + ver
        return UrlManage.buildUrl(path)

    @staticmethod
    def buildLibUrl(path):
        ver = "%s" % 201908
        path = "/lib" + path + "?Ver=" + ver
        return UrlManage.buildUrl(path)