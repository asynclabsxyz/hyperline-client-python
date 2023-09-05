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

class SavedJob(BaseModel):
    """
    SavedJob
    """
    name: StrictStr = Field(..., description="The job name.")
    type: StrictStr = Field(..., description="the job type.")
    file: StrictStr = Field(..., description="The file path of the source code.")
    package: Optional[StrictStr] = Field(None, description="The package path if applicable.")
    __properties = ["name", "type", "file", "package"]

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
    def from_json(cls, json_str: str) -> SavedJob:
        """Create an instance of SavedJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SavedJob:
        """Create an instance of SavedJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SavedJob.parse_obj(obj)

        _obj = SavedJob.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "file": obj.get("file"),
            "package": obj.get("package")
        })
        return _obj


