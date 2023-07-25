# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import hyperline_client
from hyperline_client.paths.sql_jobs import post  # noqa: E501
from hyperline_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestSqlJobs(ApiTestMixin, unittest.TestCase):
    """
    SqlJobs unit test stubs
        Submit a SQL job  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
