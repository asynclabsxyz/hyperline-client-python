<a id="__pageTop"></a>
# hyperline_client.apis.tags.dataset_api.DatasetApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_metadata**](#get_dataset_metadata) | **get** /datasets/metadata | Get dataset metadata
[**get_dataset_preview**](#get_dataset_preview) | **get** /datasets/preview | Get dataset preview
[**list_datasets**](#list_datasets) | **get** /datasets | List datasets
[**list_explorer_datasets**](#list_explorer_datasets) | **get** /datasets/explorer | List datasets for web explorer
[**list_explorer_datasets_details**](#list_explorer_datasets_details) | **get** /datasets/explorer/details | List datasets details for web explorer

# **get_dataset_metadata**
<a id="get_dataset_metadata"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_dataset_metadata(pathservice)

Get dataset metadata

Get dataset metadata.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import dataset_api
from hyperline_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'path': "path_example",
        'service': "service_example",
    }
    try:
        # Get dataset metadata
        api_response = api_instance.get_dataset_metadata(
            query_params=query_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_metadata: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path | PathSchema | | 
service | ServiceSchema | | 


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dataset_metadata.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_dataset_metadata.ApiResponseFor500) | Unknown server error.

#### get_dataset_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

#### get_dataset_metadata.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_dataset_preview**
<a id="get_dataset_preview"></a>
> SqlExecuteResponse get_dataset_preview(pathservice)

Get dataset preview

Get dataset preview.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import dataset_api
from hyperline_client.model.error import Error
from hyperline_client.model.sql_execute_response import SqlExecuteResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'path': "path_example",
        'service': "service_example",
    }
    try:
        # Get dataset preview
        api_response = api_instance.get_dataset_preview(
            query_params=query_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatasetApi->get_dataset_preview: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path | PathSchema | | 
service | ServiceSchema | | 


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ServiceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_dataset_preview.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_dataset_preview.ApiResponseFor500) | Unknown server error.

#### get_dataset_preview.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlExecuteResponse**](../../models/SqlExecuteResponse.md) |  | 


#### get_dataset_preview.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_datasets**
<a id="list_datasets"></a>
> DatasetCollection list_datasets()

List datasets

List datasets

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import dataset_api
from hyperline_client.model.dataset_collection import DatasetCollection
from hyperline_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List datasets
        api_response = api_instance.list_datasets()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatasetApi->list_datasets: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_datasets.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_datasets.ApiResponseFor500) | Unknown server error.

#### list_datasets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DatasetCollection**](../../models/DatasetCollection.md) |  | 


#### list_datasets.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_explorer_datasets**
<a id="list_explorer_datasets"></a>
> ExplorerViewDatasetCollection list_explorer_datasets()

List datasets for web explorer

List datasets for web explorer.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import dataset_api
from hyperline_client.model.error import Error
from hyperline_client.model.explorer_view_dataset_collection import ExplorerViewDatasetCollection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List datasets for web explorer
        api_response = api_instance.list_explorer_datasets()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatasetApi->list_explorer_datasets: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_explorer_datasets.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_explorer_datasets.ApiResponseFor500) | Unknown server error.

#### list_explorer_datasets.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExplorerViewDatasetCollection**](../../models/ExplorerViewDatasetCollection.md) |  | 


#### list_explorer_datasets.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_explorer_datasets_details**
<a id="list_explorer_datasets_details"></a>
> ExplorerViewDatasetCollection list_explorer_datasets_details(path)

List datasets details for web explorer

List datasets details for web explorer.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import dataset_api
from hyperline_client.model.error import Error
from hyperline_client.model.explorer_view_dataset_collection import ExplorerViewDatasetCollection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = hyperline_client.Configuration(
    host = "/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataset_api.DatasetApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'path': "path_example",
    }
    try:
        # List datasets details for web explorer
        api_response = api_instance.list_explorer_datasets_details(
            query_params=query_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatasetApi->list_explorer_datasets_details: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path | PathSchema | | 


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_explorer_datasets_details.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_explorer_datasets_details.ApiResponseFor500) | Unknown server error.

#### list_explorer_datasets_details.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExplorerViewDatasetCollection**](../../models/ExplorerViewDatasetCollection.md) |  | 


#### list_explorer_datasets_details.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

