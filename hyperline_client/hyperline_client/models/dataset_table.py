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
from pydantic import BaseModel, StrictBool, StrictStr, conlist
from hyperline_client.models.dataset_table_column import DatasetTableColumn

class DatasetTable(BaseModel):
    """
    A dataset table object.
    """
    name: Optional[StrictStr] = None
    is_view: Optional[StrictBool] = None
    columns: Optional[conlist(DatasetTableColumn)] = None
    __properties = ["name", "is_view", "columns"]

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
    def from_json(cls, json_str: str) -> DatasetTable:
        """Create an instance of DatasetTable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DatasetTable:
        """Create an instance of DatasetTable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatasetTable.parse_obj(obj)

        _obj = DatasetTable.parse_obj({
            "name": obj.get("name"),
            "is_view": obj.get("is_view"),
            "columns": [DatasetTableColumn.from_dict(_item) for _item in obj.get("columns")] if obj.get("columns") is not None else None
        })
        return _obj


