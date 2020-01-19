#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
模块功能描述：

@author Liu Mingxing
@date 2019/11/25
'''


class Site(object):
    def __init__(self):
        self.title = 'share js code'
        self.url = 'http://www.sharejs.com'

    def list_all_member(self):
        self.my_var = 1
        for name, value in vars(self).items():
            print('%s=%s' % (name, value))


if __name__ == '__main__':
    site = Site()
    site.list_all_member()
