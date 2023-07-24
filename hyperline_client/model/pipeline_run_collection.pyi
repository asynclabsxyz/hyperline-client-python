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


class PipelineRunCollection(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class pipeline_runs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PipelineRun']:
                        return PipelineRun
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['PipelineRun'], typing.List['PipelineRun']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pipeline_runs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PipelineRun':
                    return super().__getitem__(i)
            __annotations__ = {
                "pipeline_runs": pipeline_runs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pipeline_runs"]) -> MetaOapg.properties.pipeline_runs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pipeline_runs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pipeline_runs"]) -> typing.Union[MetaOapg.properties.pipeline_runs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pipeline_runs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pipeline_runs: typing.Union[MetaOapg.properties.pipeline_runs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PipelineRunCollection':
        return super().__new__(
            cls,
            *_args,
            pipeline_runs=pipeline_runs,
            _configuration=_configuration,
            **kwargs,
        )

from hyperline_client.model.pipeline_run import PipelineRun
