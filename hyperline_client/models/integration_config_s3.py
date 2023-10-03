# coding: utf-8

"""
    Hyperline API

    DO NOT EDIT THIS FILE! 

    The version of the OpenAPI document: 0.0.1
    Contact: dev@asynclabs.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictStr

class IntegrationConfigS3(BaseModel):
    """
    IntegrationConfigS3
    """
    bucket_name: Optional[StrictStr] = None
    access_key_id: Optional[StrictStr] = None
    secret_key: Optional[StrictStr] = None
    __properties = ["bucket_name", "access_key_id", "secret_key"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IntegrationConfigS3:
        """Create an instance of IntegrationConfigS3 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationConfigS3:
        """Create an instance of IntegrationConfigS3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationConfigS3.parse_obj(obj)

        _obj = IntegrationConfigS3.parse_obj({
            "bucket_name": obj.get("bucket_name"),
            "access_key_id": obj.get("access_key_id"),
            "secret_key": obj.get("secret_key")
        })
        return _obj


