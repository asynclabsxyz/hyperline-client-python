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
from hyperline_client.models.pipeline_import_error_collection import PipelineImportErrorCollection  # noqa: E501
from hyperline_client.rest import ApiException

class TestPipelineImportErrorCollection(unittest.TestCase):
    """PipelineImportErrorCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PipelineImportErrorCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PipelineImportErrorCollection`
        """
        model = hyperline_client.models.pipeline_import_error_collection.PipelineImportErrorCollection()  # noqa: E501
        if include_optional :
            return PipelineImportErrorCollection(
                pipeline_import_errors = [
                    hyperline_client.models.pipeline_import_error.PipelineImportError(
                        id = 56, 
                        timestamp = '', 
                        file_name = '', 
                        stack_trace = '', )
                    ]
            )
        else :
            return PipelineImportErrorCollection(
        )
        """

    def testPipelineImportErrorCollection(self):
        """Test PipelineImportErrorCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()