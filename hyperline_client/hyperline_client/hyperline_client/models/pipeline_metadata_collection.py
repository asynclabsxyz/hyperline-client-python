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
from hyperline_client.models.pipeline_metadata import PipelineMetadata

class PipelineMetadataCollection(BaseModel):
    """
    PipelineMetadataCollection
    """
    metadata_list: Optional[conlist(PipelineMetadata)] = None
    __properties = ["metadata_list"]

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
    def from_json(cls, json_str: str) -> PipelineMetadataCollection:
        """Create an instance of PipelineMetadataCollection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in metadata_list (list)
        _items = []
        if self.metadata_list:
            for _item in self.metadata_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metadata_list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PipelineMetadataCollection:
        """Create an instance of PipelineMetadataCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PipelineMetadataCollection.parse_obj(obj)

        _obj = PipelineMetadataCollection.parse_obj({
            "metadata_list": [PipelineMetadata.from_dict(_item) for _item in obj.get("metadata_list")] if obj.get("metadata_list") is not None else None
        })
        return _obj


