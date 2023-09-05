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
from pydantic import BaseModel, Field, StrictStr

class FileCreateRequest(BaseModel):
    """
    FileCreateRequest
    """
    file_name: StrictStr = Field(...)
    folder: Optional[StrictStr] = None
    contents: Optional[StrictStr] = None
    base64_contents: Optional[StrictStr] = None
    __properties = ["file_name", "folder", "contents", "base64_contents"]

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
    def from_json(cls, json_str: str) -> FileCreateRequest:
        """Create an instance of FileCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FileCreateRequest:
        """Create an instance of FileCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FileCreateRequest.parse_obj(obj)

        _obj = FileCreateRequest.parse_obj({
            "file_name": obj.get("file_name"),
            "folder": obj.get("folder"),
            "contents": obj.get("contents"),
            "base64_contents": obj.get("base64_contents")
        })
        return _obj


