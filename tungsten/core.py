# -*- coding: utf-8 -*-

"""
tungsten.core
~~~~~~~~~~~~~

Provides user API and response objects
"""

import requests

appid = ''

class Tungsten(object):
    def __init__(self, appid):
        self.appid = appid

    def query(self, input = ''):
        payload = {'input': input, 'appid': self.appid}
        r = requests.get("http://api.wolframalpha.com/v2/query", params=payload)
    
        return r.text

"""
_WA_app_id = ''

def app_id(appid = ''):
    _WA_app_id = appid

def query(input=''):
    payload = {'input': input, 'appid': _WA_app_id}
    r = requests.get("http://api.wolframalpha.com/v2/query", params=payload)
    print _WA_app_id
    return r.text

"""