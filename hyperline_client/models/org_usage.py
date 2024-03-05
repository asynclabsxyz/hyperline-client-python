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

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, StrictInt

class OrgUsage(BaseModel):
    """
    OrgUsage
    """
    trial_end_date: Optional[date] = Field(None, description="The date when the trial period ends.")
    trial_limit_in_cents: Optional[StrictInt] = Field(None, description="Dollar limit for trial period in cents.")
    total_usage_in_cents: Optional[StrictInt] = Field(None, description="Dollar amount used in cents.")
    bytes_scanned: Optional[StrictInt] = Field(None, description="Bytes scanned when querying data.")
    compute_units_per_ms: Optional[StrictInt] = Field(None, description="Data Compute Unit (DCU) used per millisecond.")
    bytes_stored: Optional[StrictInt] = Field(None, description="Bytes stored.")
    __properties = ["trial_end_date", "trial_limit_in_cents", "total_usage_in_cents", "bytes_scanned", "compute_units_per_ms", "bytes_stored"]

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
    def from_json(cls, json_str: str) -> OrgUsage:
        """Create an instance of OrgUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrgUsage:
        """Create an instance of OrgUsage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrgUsage.parse_obj(obj)

        _obj = OrgUsage.parse_obj({
            "trial_end_date": obj.get("trial_end_date"),
            "trial_limit_in_cents": obj.get("trial_limit_in_cents"),
            "total_usage_in_cents": obj.get("total_usage_in_cents"),
            "bytes_scanned": obj.get("bytes_scanned"),
            "compute_units_per_ms": obj.get("compute_units_per_ms"),
            "bytes_stored": obj.get("bytes_stored")
        })
        return _obj

