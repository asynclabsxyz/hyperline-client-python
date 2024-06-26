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


from typing import List, Optional
from pydantic import BaseModel, conlist
from hyperline_client.models.dataset_audit_details import DatasetAuditDetails

class DatasetAuditDetailsResponse(BaseModel):
    """
    Response object for dataset audit details.
    """
    dates: Optional[conlist(DatasetAuditDetails)] = None
    __properties = ["dates"]

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
    def from_json(cls, json_str: str) -> DatasetAuditDetailsResponse:
        """Create an instance of DatasetAuditDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in dates (list)
        _items = []
        if self.dates:
            for _item in self.dates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DatasetAuditDetailsResponse:
        """Create an instance of DatasetAuditDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasetAuditDetailsResponse.parse_obj(obj)

        _obj = DatasetAuditDetailsResponse.parse_obj({
            "dates": [DatasetAuditDetails.from_dict(_item) for _item in obj.get("dates")] if obj.get("dates") is not None else None
        })
        return _obj


