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
from hyperline_client.models.org_usage_details import OrgUsageDetails  # noqa: E501
from hyperline_client.rest import ApiException

class TestOrgUsageDetails(unittest.TestCase):
    """OrgUsageDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OrgUsageDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgUsageDetails`
        """
        model = hyperline_client.models.org_usage_details.OrgUsageDetails()  # noqa: E501
        if include_optional :
            return OrgUsageDetails(
                costs = [
                    hyperline_client.models.dated_itemized_cost.DatedItemizedCost(
                        cost = hyperline_client.models.itemized_cost.ItemizedCost(
                            bigquery = 56, 
                            gcs = 56, 
                            trino = 56, 
                            dataproc = 56, 
                            snowflake = 56, 
                            airflow = 56, 
                            jupyter = 56, 
                            gke = 56, ), 
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ]
            )
        else :
            return OrgUsageDetails(
        )
        """

    def testOrgUsageDetails(self):
        """Test OrgUsageDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
