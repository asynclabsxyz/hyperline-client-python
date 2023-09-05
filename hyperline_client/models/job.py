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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class Job(BaseModel):
    """
    A generic job object.
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    job_type: Optional[StrictStr] = None
    submitted_by: Optional[StrictStr] = None
    file: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    submitted_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    duration: Optional[StrictInt] = Field(None, description="The duration of the job in seconds.")
    __properties = ["id", "name", "job_type", "submitted_by", "file", "status", "submitted_at", "finished_at", "duration"]

    @validator('job_type')
    def job_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('pyspark', 'sql', 'trino', 'bigquery-sql', 'pipeline'):
            raise ValueError("must be one of enum values ('pyspark', 'sql', 'trino', 'bigquery-sql', 'pipeline')")
        return value

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
    def from_json(cls, json_str: str) -> Job:
        """Create an instance of Job from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Job:
        """Create an instance of Job from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Job.parse_obj(obj)

        _obj = Job.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "job_type": obj.get("job_type"),
            "submitted_by": obj.get("submitted_by"),
            "file": obj.get("file"),
            "status": obj.get("status"),
            "submitted_at": obj.get("submitted_at"),
            "finished_at": obj.get("finished_at"),
            "duration": obj.get("duration")
        })
        return _obj


