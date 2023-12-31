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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class BadUserRequest(BaseModel):
    """
    Unable to process request successfully due to input error.
    """
    bad_request: Optional[StrictBool] = None
    type: Optional[StrictStr] = None
    message: Optional[StrictStr] = Field(None, description="A human-readable explanation specific to this occurrence of the problem.")
    __properties = ["bad_request", "type", "message"]

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
    def from_json(cls, json_str: str) -> BadUserRequest:
        """Create an instance of BadUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BadUserRequest:
        """Create an instance of BadUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BadUserRequest.parse_obj(obj)

        _obj = BadUserRequest.parse_obj({
            "bad_request": obj.get("bad_request"),
            "type": obj.get("type"),
            "message": obj.get("message")
        })
        return _obj


