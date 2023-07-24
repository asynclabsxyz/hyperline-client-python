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


class Job(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A generic job object.
    """


    class MetaOapg:
        
        class properties:
            job_id = schemas.StrSchema
            user_id = schemas.StrSchema
            job_name = schemas.StrSchema
            job_type = schemas.StrSchema
            file = schemas.StrSchema
            submitted_at = schemas.DateTimeSchema
            __annotations__ = {
                "job_id": job_id,
                "user_id": user_id,
                "job_name": job_name,
                "job_type": job_type,
                "file": file,
                "submitted_at": submitted_at,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_id"]) -> MetaOapg.properties.job_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_name"]) -> MetaOapg.properties.job_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_type"]) -> MetaOapg.properties.job_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> MetaOapg.properties.file: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["submitted_at"]) -> MetaOapg.properties.submitted_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["job_id", "user_id", "job_name", "job_type", "file", "submitted_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_id"]) -> typing.Union[MetaOapg.properties.job_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_name"]) -> typing.Union[MetaOapg.properties.job_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_type"]) -> typing.Union[MetaOapg.properties.job_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union[MetaOapg.properties.file, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["submitted_at"]) -> typing.Union[MetaOapg.properties.submitted_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["job_id", "user_id", "job_name", "job_type", "file", "submitted_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        job_id: typing.Union[MetaOapg.properties.job_id, str, schemas.Unset] = schemas.unset,
        user_id: typing.Union[MetaOapg.properties.user_id, str, schemas.Unset] = schemas.unset,
        job_name: typing.Union[MetaOapg.properties.job_name, str, schemas.Unset] = schemas.unset,
        job_type: typing.Union[MetaOapg.properties.job_type, str, schemas.Unset] = schemas.unset,
        file: typing.Union[MetaOapg.properties.file, str, schemas.Unset] = schemas.unset,
        submitted_at: typing.Union[MetaOapg.properties.submitted_at, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Job':
        return super().__new__(
            cls,
            *_args,
            job_id=job_id,
            user_id=user_id,
            job_name=job_name,
            job_type=job_type,
            file=file,
            submitted_at=submitted_at,
            _configuration=_configuration,
            **kwargs,
        )
