# coding: utf-8

"""
    Hyperline API

    DO NOT EDIT THIS FILE! 

    The version of the OpenAPI document: 0.0.1
    Contact: dev@asynclabs.xyz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr

from typing import Optional

from hyperline_client.models.job_collection import JobCollection

from hyperline_client.api_client import ApiClient
from hyperline_client.api_response import ApiResponse
from hyperline_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def list_jobs2(self, isactive : Annotated[Optional[StrictBool], Field(description="should the job be in active state")] = None, type : Annotated[Optional[StrictStr], Field(description="The type of the job/file.")] = None, status : Optional[StrictStr] = None, creator : Annotated[Optional[StrictStr], Field(description="creator of the job")] = None, **kwargs) -> JobCollection:  # noqa: E501
        """List user jobs  # noqa: E501

        List jobs matching the filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_jobs2(isactive, type, status, creator, async_req=True)
        >>> result = thread.get()

        :param isactive: should the job be in active state
        :type isactive: bool
        :param type: The type of the job/file.
        :type type: str
        :param status:
        :type status: str
        :param creator: creator of the job
        :type creator: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: JobCollection
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_jobs2_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_jobs2_with_http_info(isactive, type, status, creator, **kwargs)  # noqa: E501

    @validate_arguments
    def list_jobs2_with_http_info(self, isactive : Annotated[Optional[StrictBool], Field(description="should the job be in active state")] = None, type : Annotated[Optional[StrictStr], Field(description="The type of the job/file.")] = None, status : Optional[StrictStr] = None, creator : Annotated[Optional[StrictStr], Field(description="creator of the job")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List user jobs  # noqa: E501

        List jobs matching the filter.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_jobs2_with_http_info(isactive, type, status, creator, async_req=True)
        >>> result = thread.get()

        :param isactive: should the job be in active state
        :type isactive: bool
        :param type: The type of the job/file.
        :type type: str
        :param status:
        :type status: str
        :param creator: creator of the job
        :type creator: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(JobCollection, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'isactive',
            'type',
            'status',
            'creator'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_jobs2" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('isactive') is not None:  # noqa: E501
            _query_params.append(('isactive', _params['isactive']))

        if _params.get('type') is not None:  # noqa: E501
            _query_params.append(('type', _params['type']))

        if _params.get('status') is not None:  # noqa: E501
            _query_params.append(('status', _params['status']))

        if _params.get('creator') is not None:  # noqa: E501
            _query_params.append(('creator', _params['creator']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['bearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "JobCollection",
            '500': "Error",
        }

        return self.api_client.call_api(
            '/jobs', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))