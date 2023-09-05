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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class PipelineRun(BaseModel):
    """
    A run of a pipeline.
    """
    pipeline_name: StrictStr = Field(...)
    run_id: StrictStr = Field(...)
    state: Optional[StrictStr] = None
    logical_date: Optional[datetime] = None
    config: Optional[Dict[str, Any]] = None
    __properties = ["pipeline_name", "run_id", "state", "logical_date", "config"]

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
    def from_json(cls, json_str: str) -> PipelineRun:
        """Create an instance of PipelineRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PipelineRun:
        """Create an instance of PipelineRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PipelineRun.parse_obj(obj)

        _obj = PipelineRun.parse_obj({
            "pipeline_name": obj.get("pipeline_name"),
            "run_id": obj.get("run_id"),
            "state": obj.get("state"),
            "logical_date": obj.get("logical_date"),
            "config": obj.get("config")
        })
        return _obj


