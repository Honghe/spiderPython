#!usr/bin/env python
# encoding: utf-8

'''爬一个简单的网页，并下载网页中的mp3文件

    存在的问题是：
    1. 下载mp3文件模块未实现，所以先以wget小工具顶上
    2. 在问题1的情况下，保存的bat文件是UFT-8编码，其运行时处理非英文字符时有问题
'''
import urllib

__author__ = 'honghe'

import re
import requests
from os.path import dirname, abspath

PREFIX = dirname(abspath(__file__))

def extract(begin, end, data):
    '''抽取行内begin与end之间的内容

    '''
    result = []
    r = re.compile(r'.+%s(.+?)%s.+' % (begin, end))
    li = data.split('\r\n')
    for l in li:
        m = r.match(l)
        if m:
            print m.group(1)
            result.append(m.group(1))
    return result


def fetch():
    '''获取网页中的mp3地址与名字

    '''

#    保存成简单bat文件
    with open("%s/down.bat" % PREFIX, 'w') as down:
#        只选几个页面做测试
        for i in xrange(395, 396):
            url = 'http://www.luoo.net/radio/radio%s/mp3.xml' % i
            r = requests.get(url)
            if r.status_code == 200:
                for path, name in zip(
                    extract('path="', '"', r.content),
                    extract('title="', '"', r.content)
                ):
                    urllib.urlretrieve(path, )


if __name__ == '__main__':
    fetch()