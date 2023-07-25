<a id="__pageTop"></a>
# hyperline_client.apis.tags.job_api.JobApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_jobs**](#list_jobs) | **get** /jobs | List user jobs

# **list_jobs**
<a id="list_jobs"></a>
> JobCollection list_jobs()

List user jobs

List all jobs of the user.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import job_api
from hyperline_client.model.error import Error
from hyperline_client.model.job_collection import JobCollection
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_api.JobApi(api_client)

    # example passing only optional values
    query_params = {
        'file': "file_example",
        'type': "pyspark",
        'name': "name_example",
        'limit': 1,
    }
    try:
        # List user jobs
        api_response = api_instance.list_jobs(
            query_params=query_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling JobApi->list_jobs: %s\n" % e)
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
file | FileSchema | | optional
type | TypeSchema | | optional
name | NameSchema | | optional
limit | LimitSchema | | optional


# FileSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["pyspark", "sql", "bigquery-sql", ] 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_jobs.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_jobs.ApiResponseFor500) | Unknown server error.

#### list_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobCollection**](../../models/JobCollection.md) |  | 


#### list_jobs.ApiResponseFor500
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

