# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import hyperline_hyperline_client.client
from hyperline_hyperline_client.client.paths.pipelines_pipeline_name_runs_run_id_stages_stage_name_logs_try_number import get  # noqa: E501
from hyperline_hyperline_client.client import configuration, schemas, api_hyperline_client.client

from .. import ApiTestMixin


class TestPipelinesPipelineNameRunsRunIdStagesStageNameLogsTryNumber(ApiTestMixin, unittest.TestCase):
    """
    PipelinesPipelineNameRunsRunIdStagesStageNameLogsTryNumber unit test stubs
        Get the logs of a pipeline stage instance  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_hyperline_client.client = api_hyperline_client.client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_hyperline_client.client=used_api_hyperline_client.client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
