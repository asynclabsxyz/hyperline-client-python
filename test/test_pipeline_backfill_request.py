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
import datetime

import hyperline_client
from hyperline_client.models.pipeline_backfill_request import PipelineBackfillRequest  # noqa: E501
from hyperline_client.rest import ApiException

class TestPipelineBackfillRequest(unittest.TestCase):
    """PipelineBackfillRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PipelineBackfillRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PipelineBackfillRequest`
        """
        model = hyperline_client.models.pipeline_backfill_request.PipelineBackfillRequest()  # noqa: E501
        if include_optional :
            return PipelineBackfillRequest(
                pipeline_name = '', 
                argument_name = '', 
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                interval = 56
            )
        else :
            return PipelineBackfillRequest(
                pipeline_name = '',
                argument_name = '',
                start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )
        """

    def testPipelineBackfillRequest(self):
        """Test PipelineBackfillRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
