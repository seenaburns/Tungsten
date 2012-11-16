#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tungsten Test Suite
~~~~~~~~~~~~~~~~~~~

A series of unittests to check the basic functionality of the Tungsten API.

NOTE: Test suite could use some attention with a more methodical approach
to testing results and important edge cases.

"""

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

    def test_error_appid(self):
        """
        Test error response of a faulty appid
        """

        client = tungsten.Tungsten('XXXX')
        result = client.query('pi')

        self.assertFalse(result.success)
        self.assertEqual(result.error, 'Invalid appid')

    def test_pi(self):
        """
        Test repsonse of a standard query, namely the API functionality
        """

        client = tungsten.Tungsten(appid)
        result = client.query('pi')

        self.assertTrue(result.success)
        self.assertEqual(result.error, None)

        # Pod information expected to be returned
        expected_titles = ['Input',
                           'Decimal approximation',
                           'Property',
                           'Number line',
                           'Continued fraction',
                           'Alternative representations',
                           'Series representations',
                           'Integral representations']
        expected_ids = ['Input',
                        'DecimalApproximation',
                        'Property',
                        'NumberLine',
                        'ContinuedFraction',
                        'AlternativeRepresentations:MathematicalFunctionIdentityData',
                        'SeriesRepresentations:MathematicalFunctionIdentityData',
                        'IntegralRepresentations:MathematicalFunctionIdentityData']
        expected_scanners = ['Identity',
                             'Numeric',
                             'Numeric',
                             'NumberLine',
                             'ContinuedFraction',
                             'MathematicalFunctionData',
                             'MathematicalFunctionData',
                             'MathematicalFunctionData']

        # Returned pod information
        titles = [pod.title for pod in result.pods]
        ids = [pod.id for pod in result.pods]
        scanners = [pod.scanner for pod in result.pods]

        self.assertEqual(titles, expected_titles)
        self.assertEqual(ids, expected_ids)
        self.assertEqual(scanners, expected_scanners)

    def test_params(self):
        """
        Test query / response of query with specified parameters
        """
        client = tungsten.Tungsten(appid)

        # Parameters as list and as string
        params = {'format': ['minput', 'moutput'], 'scanner': 'numeric'}

        result = client.query('pi', params)
        
        for pod in result.pods:
            self.assertIn(pod.scanner, ['Numeric'])
            for format in pod.format:
                self.assertIn(format, ['minput', 'moutput'])   

        self.assertEqual(result.pods[0].format['minput'], ['N[Pi, 71]'])
        self.assertEqual(result.pods[1].format['minput'], ['Element[Pi, Algebraics]'])

if __name__ == '__main__':
    # Get appid from first argument of commandline
    appid = sys.argv[1]

    # Change sys.argv back to rest of arguments for unit test
    sys.argv[1:] = sys.argv[2:]

    # Run unit tests
    unittest.main()
