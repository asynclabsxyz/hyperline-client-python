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
from hyperline_client.api.invitation_api import InvitationApi  # noqa: E501
from hyperline_client.rest import ApiException


class TestInvitationApi(unittest.TestCase):
    """InvitationApi unit test stubs"""

    def setUp(self):
        self.api = hyperline_client.api.invitation_api.InvitationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_verify_invitation(self):
        """Test case for verify_invitation

        Verifies an invitation and onboards.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
