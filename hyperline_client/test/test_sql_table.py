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
from hyperline_client.models.sql_table import SqlTable  # noqa: E501
from hyperline_client.rest import ApiException

class TestSqlTable(unittest.TestCase):
    """SqlTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SqlTable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SqlTable`
        """
        model = hyperline_client.models.sql_table.SqlTable()  # noqa: E501
        if include_optional :
            return SqlTable(
                name = '', 
                columns = [
                    hyperline_client.models.sql_column.SqlColumn(
                        name = '', 
                        type = '', 
                        nullable = '', )
                    ]
            )
        else :
            return SqlTable(
        )
        """

    def testSqlTable(self):
        """Test SqlTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()