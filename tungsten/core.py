# -*- coding: utf-8 -*-

"""
tungsten.core
~~~~~~~~~~~~~

Provides user API and response objects
"""

import requests
from xml.etree.ElementTree import fromstring, ElementTree

class Tungsten(object):
    def __init__(self, appid):
        self.appid = appid

    def query(self, input = ''):
        # Compose query and get
        payload = {'input': input, 'appid': self.appid}
        r = requests.get("http://api.wolframalpha.com/v2/query", params=payload)

        # Exit if request error
        if r.status_code != 200 or r.encoding != 'utf-8':
            return None

        # Construct Result object from XML Result
        # ElementTree.fromstring requires byte code, so encode r.text
        return Result(r.text.encode('utf-8'))

class Result(object):
    def __init__(self, xml_result = None):
        # Construct XML tree
        self.xml_tree = ElementTree(fromstring(xml_result))

    @property
    def success(self):
        # Success from queryresult
        return self.xml_tree.getroot().get('success') == 'true'

    @property
    def error(self):
        # Error from XML group
        error = self.xml_tree.find('error')
        if error is not None:
            return error.find('msg').text
        return None