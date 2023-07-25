# coding: utf-8

"""
    Hyperline API

    DO NOT EDIT THIS FILE!   # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: dev@asynclabs.xyz
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from hyperline_client import schemas  # noqa: F401


class SqlJobStatistics(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            start_time = schemas.DateTimeSchema
            end_time = schemas.DateTimeSchema
            duration = schemas.Int64Schema
            total_bytes_processed = schemas.Int64Schema
            __annotations__ = {
                "start_time": start_time,
                "end_time": end_time,
                "duration": duration,
                "total_bytes_processed": total_bytes_processed,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_time"]) -> MetaOapg.properties.start_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_time"]) -> MetaOapg.properties.end_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_bytes_processed"]) -> MetaOapg.properties.total_bytes_processed: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["start_time", "end_time", "duration", "total_bytes_processed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_time"]) -> typing.Union[MetaOapg.properties.start_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_time"]) -> typing.Union[MetaOapg.properties.end_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_bytes_processed"]) -> typing.Union[MetaOapg.properties.total_bytes_processed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["start_time", "end_time", "duration", "total_bytes_processed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        start_time: typing.Union[MetaOapg.properties.start_time, str, datetime, schemas.Unset] = schemas.unset,
        end_time: typing.Union[MetaOapg.properties.end_time, str, datetime, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        total_bytes_processed: typing.Union[MetaOapg.properties.total_bytes_processed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SqlJobStatistics':
        return super().__new__(
            cls,
            *_args,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            total_bytes_processed=total_bytes_processed,
            _configuration=_configuration,
            **kwargs,
        )
