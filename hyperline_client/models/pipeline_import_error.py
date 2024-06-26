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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PipelineImportError(BaseModel):
    """
    A pipeline import error.
    """
    id: Optional[StrictInt] = Field(None, description="The import error ID.")
    timestamp: Optional[StrictStr] = Field(None, description="The time when this error was created.")
    file_name: Optional[StrictStr] = Field(None, description="The file name of the associated DAG file.")
    stack_trace: Optional[StrictStr] = Field(None, description="The full stackstrace from Airflow.")
    __properties = ["id", "timestamp", "file_name", "stack_trace"]

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
    def from_json(cls, json_str: str) -> PipelineImportError:
        """Create an instance of PipelineImportError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PipelineImportError:
        """Create an instance of PipelineImportError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PipelineImportError.parse_obj(obj)

        _obj = PipelineImportError.parse_obj({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "file_name": obj.get("file_name"),
            "stack_trace": obj.get("stack_trace")
        })
        return _obj


