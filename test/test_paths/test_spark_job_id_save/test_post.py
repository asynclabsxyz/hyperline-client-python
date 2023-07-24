# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import hyperline_hyperline_client.client
from hyperline_hyperline_client.client.paths.spark_job_id_save import post  # noqa: E501
from hyperline_hyperline_client.client import configuration, schemas, api_hyperline_client.client

from .. import ApiTestMixin


class TestSparkJobIdSave(ApiTestMixin, unittest.TestCase):
    """
    SparkJobIdSave unit test stubs
        Save a spark job for pipeline  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_hyperline_client.client = api_hyperline_client.client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_hyperline_client.client=used_api_hyperline_client.client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
