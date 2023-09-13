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
from hyperline_client.api.file_api import FileApi  # noqa: E501
from hyperline_client.rest import ApiException


class TestFileApi(unittest.TestCase):
    """FileApi unit test stubs"""

    def setUp(self):
        self.api = hyperline_client.api.file_api.FileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_file(self):
        """Test case for create_file

        Create a file  # noqa: E501
        """
        pass

    def test_get_file_content(self):
        """Test case for get_file_content

        Get file content  # noqa: E501
        """
        pass

    def test_get_file_metadata(self):
        """Test case for get_file_metadata

        Get file metadata  # noqa: E501
        """
        pass

    def test_get_file_preview(self):
        """Test case for get_file_preview

        Get file preview  # noqa: E501
        """
        pass

    def test_get_samples(self):
        """Test case for get_samples

        Get sample files  # noqa: E501
        """
        pass

    def test_list_files(self):
        """Test case for list_files

        List files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()