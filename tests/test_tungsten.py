#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import argparse

# Path hack. (for importing)
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import tungsten

appid = ''

class TungstenTestSuite(unittest.TestCase):

    def setUp(self):
        self.appid = appid

    # Test error response
    def test_error_appid(self):
        client = tungsten.Tungsten('XXXX')
        result = client.query('pi')
        self.assertFalse(result.success)
        self.assertEqual(result.error, 'Invalid appid')

    def test_pi(self):
        client = tungsten.Tungsten(appid)
        result = client.query('pi')
        self.assertTrue(result.success)
        self.assertEqual(result.error, None)

if __name__ == '__main__':
    # Get appid from first argument of commandline
    appid = sys.argv[1]

    # Change sys.argv back to rest of arguments for unit test
    sys.argv[1:] = sys.argv[2:]

    # Run unit tests
    unittest.main()
