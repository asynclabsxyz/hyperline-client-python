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



from pydantic import BaseModel, Field, StrictStr

class SparkJobSaveRequest(BaseModel):
    """
    A request object for saving a Spark job to pipeline.
    """
    pipeline_name: StrictStr = Field(...)
    schedule: StrictStr = Field(...)
    __properties = ["pipeline_name", "schedule"]

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
    def from_json(cls, json_str: str) -> SparkJobSaveRequest:
        """Create an instance of SparkJobSaveRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SparkJobSaveRequest:
        """Create an instance of SparkJobSaveRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SparkJobSaveRequest.parse_obj(obj)

        _obj = SparkJobSaveRequest.parse_obj({
            "pipeline_name": obj.get("pipeline_name"),
            "schedule": obj.get("schedule")
        })
        return _obj


