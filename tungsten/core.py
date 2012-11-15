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
        """Create a Tungsten object with a set appid"""
        self.appid = appid

    def query(self, input = ''):
        """Query Wolfram Alpha and return a Result object"""
        # Catch any issues with connecting to Wolfram Alpha API
        try:
            payload = {'input': input, 'appid': self.appid}
            r = requests.get("http://api.wolframalpha.com/v2/query", params=payload)

            # Raise Exception (to be returned as error)
            if r.status_code != 200:
                raise Exception('Invalid response status code: %s' % (r.status_code))
            if r.encoding != 'utf-8':
                raise Exception('Invalid encoding: %s' % (r.encoding))

        except Exception, e:
            return Result(error = e)

        return Result(xml = r.text)

class Result(object):
    def __init__(self, xml = '', error = None):
        # ElementTree.fromstring is fragile
        #   Requires byte code, so encode into utf-8
        #   Cannot handle None type, so check if xml exists
        self.xml_tree = None
        if xml:
            self.xml_tree = ElementTree(fromstring(xml.encode('utf-8')))

        # Pass any errors from requesting query along
        self.error_msg = error

    @property
    def success(self):
        # Success from queryresult
        if not self.error_msg:
            return self.xml_tree.getroot().get('success') == 'true'
        else:
            return False

    @property
    def error(self):
        # Check for errors from requesting query
        if self.error_msg:
            return self.error_msg

        # Error from XML group
        error = self.xml_tree.find('error')
        if error is not None:
            return error.find('msg').text
        return None