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
from hyperline_client.models.sql_job_statistics import SqlJobStatistics

class SqlJobDetails(BaseModel):
    """
    A SQL job status object.
    """
    job_id: StrictStr = Field(...)
    engine: Optional[StrictStr] = None
    query: Optional[StrictStr] = None
    job_status: StrictStr = Field(...)
    submitted_by: Optional[StrictStr] = None
    statistics: Optional[SqlJobStatistics] = None
    __properties = ["job_id", "engine", "query", "job_status", "submitted_by", "statistics"]

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
    def from_json(cls, json_str: str) -> SqlJobDetails:
        """Create an instance of SqlJobDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SqlJobDetails:
        """Create an instance of SqlJobDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SqlJobDetails.parse_obj(obj)

        _obj = SqlJobDetails.parse_obj({
            "job_id": obj.get("job_id"),
            "engine": obj.get("engine"),
            "query": obj.get("query"),
            "job_status": obj.get("job_status"),
            "submitted_by": obj.get("submitted_by"),
            "statistics": SqlJobStatistics.from_dict(obj.get("statistics")) if obj.get("statistics") is not None else None
        })
        return _obj


