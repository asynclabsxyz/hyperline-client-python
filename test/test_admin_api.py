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
from hyperline_client.api.admin_api import AdminApi  # noqa: E501
from hyperline_client.rest import ApiException


class TestAdminApi(unittest.TestCase):
    """AdminApi unit test stubs"""

    def setUp(self):
        self.api = hyperline_client.api.admin_api.AdminApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_enable_airflow(self):
        """Test case for enable_airflow

        Enable airflow  # noqa: E501
        """
        pass

    def test_enable_jupyter(self):
        """Test case for enable_jupyter

        Enable jupyter  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
