<a id="__pageTop"></a>
# hyperline_client.apis.tags.sql_api.SqlApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_sql_job**](#check_sql_job) | **get** /sql/jobs/{job_id}/status | Check the status of a SQL job
[**execute_sql_query**](#execute_sql_query) | **post** /sql | Execute a SQL query
[**get_sql_cache**](#get_sql_cache) | **get** /sql/edit | Get user SQL query cache
[**get_sql_job_output**](#get_sql_job_output) | **get** /sql/jobs/{job_id}/output | Get the output of a SQL job
[**get_sql_queries**](#get_sql_queries) | **get** /sql/queries | Get user SQL queries
[**submit_sql_job**](#submit_sql_job) | **post** /sql/jobs | Submit a SQL job
[**update_sql_cache**](#update_sql_cache) | **post** /sql/edit | Update user SQL query cache
[**update_sql_query**](#update_sql_query) | **post** /sql/queries | Update user SQL query cache

# **check_sql_job**
<a id="check_sql_job"></a>
> SqlJobStatus check_sql_job(job_id)

Check the status of a SQL job

Check the status of a SQL job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_job_status import SqlJobStatus
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Check the status of a SQL job
        api_response = api_instance.check_sql_job(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->check_sql_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_sql_job.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#check_sql_job.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#check_sql_job.ApiResponseFor500) | Unknown server error.

#### check_sql_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlJobStatus**](../../models/SqlJobStatus.md) |  | 


#### check_sql_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### check_sql_job.ApiResponseFor500
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

# **execute_sql_query**
<a id="execute_sql_query"></a>
> SqlExecuteResponse execute_sql_query(sql_query)

Execute a SQL query

Execute a SQL query.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_query import SqlQuery
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    body = SqlQuery(
        name="name_example",
        types=[
            "types_example"
        ],
        statement="statement_example",
        id=1,
    )
    try:
        # Execute a SQL query
        api_response = api_instance.execute_sql_query(
            body=body,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->execute_sql_query: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#execute_sql_query.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#execute_sql_query.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#execute_sql_query.ApiResponseFor500) | Unknown server error.

#### execute_sql_query.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlExecuteResponse**](../../models/SqlExecuteResponse.md) |  | 


#### execute_sql_query.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### execute_sql_query.ApiResponseFor500
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

# **get_sql_cache**
<a id="get_sql_cache"></a>
> SqlQuery get_sql_cache()

Get user SQL query cache

Get user SQL query cache.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_query import SqlQuery
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
    api_instance = sql_api.SqlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user SQL query cache
        api_response = api_instance.get_sql_cache()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->get_sql_cache: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sql_cache.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_sql_cache.ApiResponseFor500) | Unknown server error.

#### get_sql_cache.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


#### get_sql_cache.ApiResponseFor500
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

# **get_sql_job_output**
<a id="get_sql_job_output"></a>
> SqlExecuteResponse get_sql_job_output(job_id)

Get the output of a SQL job

Get the output of a SQL job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Get the output of a SQL job
        api_response = api_instance.get_sql_job_output(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->get_sql_job_output: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
job_id | JobIdSchema | | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sql_job_output.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#get_sql_job_output.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#get_sql_job_output.ApiResponseFor500) | Unknown server error.

#### get_sql_job_output.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlExecuteResponse**](../../models/SqlExecuteResponse.md) |  | 


#### get_sql_job_output.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_sql_job_output.ApiResponseFor500
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

# **get_sql_queries**
<a id="get_sql_queries"></a>
> SqlQueryCollection get_sql_queries()

Get user SQL queries

Get user SQL queries from DB.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.error import Error
from hyperline_client.model.sql_query_collection import SqlQueryCollection
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
    api_instance = sql_api.SqlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user SQL queries
        api_response = api_instance.get_sql_queries()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->get_sql_queries: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sql_queries.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_sql_queries.ApiResponseFor500) | Unknown server error.

#### get_sql_queries.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQueryCollection**](../../models/SqlQueryCollection.md) |  | 


#### get_sql_queries.ApiResponseFor500
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

# **submit_sql_job**
<a id="submit_sql_job"></a>
> SqlExecuteResponse submit_sql_job(sql_query)

Submit a SQL job

Submit a SQL job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_query import SqlQuery
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    body = SqlQuery(
        name="name_example",
        types=[
            "types_example"
        ],
        statement="statement_example",
        id=1,
    )
    try:
        # Submit a SQL job
        api_response = api_instance.submit_sql_job(
            body=body,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->submit_sql_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#submit_sql_job.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#submit_sql_job.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#submit_sql_job.ApiResponseFor500) | Unknown server error.

#### submit_sql_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlExecuteResponse**](../../models/SqlExecuteResponse.md) |  | 


#### submit_sql_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### submit_sql_job.ApiResponseFor500
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

# **update_sql_cache**
<a id="update_sql_cache"></a>
> update_sql_cache(sql_query)

Update user SQL query cache

Update user SQL query cache.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_query import SqlQuery
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    body = SqlQuery(
        name="name_example",
        types=[
            "types_example"
        ],
        statement="statement_example",
        id=1,
    )
    try:
        # Update user SQL query cache
        api_response = api_instance.update_sql_cache(
            body=body,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->update_sql_cache: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_sql_cache.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#update_sql_cache.ApiResponseFor500) | Unknown server error.

#### update_sql_cache.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_sql_cache.ApiResponseFor500
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

# **update_sql_query**
<a id="update_sql_query"></a>
> SqlQuery update_sql_query(sql_query)

Update user SQL query cache

Update user SQL query cache.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import sql_api
from hyperline_client.model.sql_query import SqlQuery
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
    api_instance = sql_api.SqlApi(api_client)

    # example passing only required values which don't have defaults set
    body = SqlQuery(
        name="name_example",
        types=[
            "types_example"
        ],
        statement="statement_example",
        id=1,
    )
    try:
        # Update user SQL query cache
        api_response = api_instance.update_sql_query(
            body=body,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SqlApi->update_sql_query: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_sql_query.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#update_sql_query.ApiResponseFor500) | Unknown server error.

#### update_sql_query.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlQuery**](../../models/SqlQuery.md) |  | 


#### update_sql_query.ApiResponseFor500
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

