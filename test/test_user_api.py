# coding: utf-8

"""
    Hyperline API

    DO NOT EDIT THIS FILE! 

    The version of the OpenAPI document: 0.0.1
    Contact: dev@asynclabs.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import hyperline_client
from hyperline_client.api.user_api import UserApi  # noqa: E501
from hyperline_client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = hyperline_client.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
