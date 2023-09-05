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
from hyperline_client.models.spark_job_collection import SparkJobCollection  # noqa: E501
from hyperline_client.rest import ApiException

class TestSparkJobCollection(unittest.TestCase):
    """SparkJobCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SparkJobCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SparkJobCollection`
        """
        model = hyperline_client.models.spark_job_collection.SparkJobCollection()  # noqa: E501
        if include_optional :
            return SparkJobCollection(
                spark_jobs = [
                    hyperline_client.models.spark_job.SparkJob(
                        id = '', 
                        name = '', 
                        file = '', 
                        type = '', 
                        status = '', 
                        submitted_by = '', 
                        submitted_on = '', 
                        duration = 56, )
                    ]
            )
        else :
            return SparkJobCollection(
        )
        """

    def testSparkJobCollection(self):
        """Test SparkJobCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
