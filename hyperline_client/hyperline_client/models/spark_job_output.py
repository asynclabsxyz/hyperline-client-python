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

class SparkJobOutput(BaseModel):
    """
    SparkJobOutput
    """
    job_id: StrictStr = Field(...)
    job_type: Optional[StrictStr] = None
    job_status: StrictStr = Field(...)
    status_timestamp: Optional[StrictStr] = None
    job_output: Optional[StrictStr] = None
    __properties = ["job_id", "job_type", "job_status", "status_timestamp", "job_output"]

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
    def from_json(cls, json_str: str) -> SparkJobOutput:
        """Create an instance of SparkJobOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SparkJobOutput:
        """Create an instance of SparkJobOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SparkJobOutput.parse_obj(obj)

        _obj = SparkJobOutput.parse_obj({
            "job_id": obj.get("job_id"),
            "job_type": obj.get("job_type"),
            "job_status": obj.get("job_status"),
            "status_timestamp": obj.get("status_timestamp"),
            "job_output": obj.get("job_output")
        })
        return _obj


