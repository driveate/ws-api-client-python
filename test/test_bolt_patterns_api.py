# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ws_api_client
from ws_api_client.api.bolt_patterns_api import BoltPatternsApi  # noqa: E501
from ws_api_client.rest import ApiException


class TestBoltPatternsApi(unittest.TestCase):
    """BoltPatternsApi unit test stubs"""

    def setUp(self):
        self.api = ws_api_client.api.bolt_patterns_api.BoltPatternsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bolt_patterns_list(self):
        """Test case for bolt_patterns_list

        Get list of bolt patterns  # noqa: E501
        """
        pass

    def test_bolt_patterns_read(self):
        """Test case for bolt_patterns_read

        Model modifications by bolt pattern  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
