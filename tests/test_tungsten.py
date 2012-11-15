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
    # Get appid from command line
    parser = argparse.ArgumentParser(description='Tungsten Test Suite')
    parser.add_argument('appid', help='AppID')
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()

    appid = args.appid

    # Change sys.argv back to rest of arguments for unit test
    sys.argv[1:] = args.unittest_args

    # Run unit tests
    unittest.main()
