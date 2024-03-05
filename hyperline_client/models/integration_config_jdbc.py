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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class IntegrationConfigJDBC(BaseModel):
    """
    IntegrationConfigJDBC
    """
    user: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    tcp_host: Optional[StrictStr] = None
    port: Optional[Union[StrictFloat, StrictInt]] = None
    database: Optional[StrictStr] = None
    __properties = ["user", "password", "tcp_host", "port", "database"]

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
    def from_json(cls, json_str: str) -> IntegrationConfigJDBC:
        """Create an instance of IntegrationConfigJDBC from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IntegrationConfigJDBC:
        """Create an instance of IntegrationConfigJDBC from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IntegrationConfigJDBC.parse_obj(obj)

        _obj = IntegrationConfigJDBC.parse_obj({
            "user": obj.get("user"),
            "password": obj.get("password"),
            "tcp_host": obj.get("tcp_host"),
            "port": obj.get("port"),
            "database": obj.get("database")
        })
        return _obj

