<a id="__pageTop"></a>
# hyperline_client.apis.tags.spark_api.SparkApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spark_cancel_job**](#spark_cancel_job) | **post** /spark/{job_id}/cancel | Cancel a Spark job
[**spark_check_job**](#spark_check_job) | **get** /spark/{job_id} | Check a Spark job status
[**spark_get_job_output**](#spark_get_job_output) | **get** /spark/{job_id}/output | Get Spark job output
[**spark_get_sql**](#spark_get_sql) | **get** /sparksql/edit | Get user Spark SQL query cache
[**spark_list_jobs**](#spark_list_jobs) | **get** /spark | List Spark jobs
[**spark_list_saved_jobs**](#spark_list_saved_jobs) | **get** /spark/jobs/saved | List saved spark jobs
[**spark_save_job**](#spark_save_job) | **post** /spark/{job_id}/save | Save a spark job for pipeline
[**spark_submit_job**](#spark_submit_job) | **post** /spark | Submit a Spark job
[**spark_submit_sql**](#spark_submit_sql) | **post** /sparksql | Submit a Spark SQL job
[**spark_update_sql**](#spark_update_sql) | **post** /sparksql/edit | Update user Spark SQL query cache

# **spark_cancel_job**
<a id="spark_cancel_job"></a>
> SparkJobStatus spark_cancel_job(job_id)

Cancel a Spark job

Cancel a Spark job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.spark_job_status import SparkJobStatus
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Cancel a Spark job
        api_response = api_instance.spark_cancel_job(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_cancel_job: %s\n" % e)
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
200 | [ApiResponseFor200](#spark_cancel_job.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#spark_cancel_job.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#spark_cancel_job.ApiResponseFor500) | Unknown server error.

#### spark_cancel_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SparkJobStatus**](../../models/SparkJobStatus.md) |  | 


#### spark_cancel_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### spark_cancel_job.ApiResponseFor500
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

# **spark_check_job**
<a id="spark_check_job"></a>
> SparkJobStatus spark_check_job(job_id)

Check a Spark job status

Check the status of a Spark job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.spark_job_status import SparkJobStatus
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Check a Spark job status
        api_response = api_instance.spark_check_job(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_check_job: %s\n" % e)
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
200 | [ApiResponseFor200](#spark_check_job.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#spark_check_job.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#spark_check_job.ApiResponseFor500) | Unknown server error.

#### spark_check_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SparkJobStatus**](../../models/SparkJobStatus.md) |  | 


#### spark_check_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### spark_check_job.ApiResponseFor500
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

# **spark_get_job_output**
<a id="spark_get_job_output"></a>
> SparkJobOutput spark_get_job_output(job_id)

Get Spark job output

Get output data from a Spark job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.spark_job_output import SparkJobOutput
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Get Spark job output
        api_response = api_instance.spark_get_job_output(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_get_job_output: %s\n" % e)
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
200 | [ApiResponseFor200](#spark_get_job_output.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#spark_get_job_output.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#spark_get_job_output.ApiResponseFor500) | Unknown server error.

#### spark_get_job_output.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SparkJobOutput**](../../models/SparkJobOutput.md) |  | 


#### spark_get_job_output.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### spark_get_job_output.ApiResponseFor500
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

# **spark_get_sql**
<a id="spark_get_sql"></a>
> File spark_get_sql()

Get user Spark SQL query cache

Get user Spark SQL query cache.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.file import File
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
    api_instance = spark_api.SparkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get user Spark SQL query cache
        api_response = api_instance.spark_get_sql()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_get_sql: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#spark_get_sql.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#spark_get_sql.ApiResponseFor500) | Unknown server error.

#### spark_get_sql.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**File**](../../models/File.md) |  | 


#### spark_get_sql.ApiResponseFor500
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

# **spark_list_jobs**
<a id="spark_list_jobs"></a>
> SparkJobCollection spark_list_jobs()

List Spark jobs

List Spark jobs.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.spark_job_collection import SparkJobCollection
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
    api_instance = spark_api.SparkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Spark jobs
        api_response = api_instance.spark_list_jobs()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_list_jobs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#spark_list_jobs.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#spark_list_jobs.ApiResponseFor500) | Unknown server error.

#### spark_list_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SparkJobCollection**](../../models/SparkJobCollection.md) |  | 


#### spark_list_jobs.ApiResponseFor500
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

# **spark_list_saved_jobs**
<a id="spark_list_saved_jobs"></a>
> SavedJobCollection spark_list_saved_jobs()

List saved spark jobs

List saved spark jobs.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.saved_job_collection import SavedJobCollection
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
    api_instance = spark_api.SparkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List saved spark jobs
        api_response = api_instance.spark_list_saved_jobs()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_list_saved_jobs: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#spark_list_saved_jobs.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#spark_list_saved_jobs.ApiResponseFor500) | Unknown server error.

#### spark_list_saved_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SavedJobCollection**](../../models/SavedJobCollection.md) |  | 


#### spark_list_saved_jobs.ApiResponseFor500
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

# **spark_save_job**
<a id="spark_save_job"></a>
> spark_save_job(job_id)

Save a spark job for pipeline

Save a spark job to pipeline jobs directory.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'job_id': "job_id_example",
    }
    try:
        # Save a spark job for pipeline
        api_response = api_instance.spark_save_job(
            path_params=path_params,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_save_job: %s\n" % e)
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
204 | [ApiResponseFor204](#spark_save_job.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#spark_save_job.ApiResponseFor500) | Unknown server error.

#### spark_save_job.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### spark_save_job.ApiResponseFor500
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

# **spark_submit_job**
<a id="spark_submit_job"></a>
> SparkJobStatus spark_submit_job(spark_job_submit_request)

Submit a Spark job

Submit a Spark job.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.spark_job_submit_request import SparkJobSubmitRequest
from hyperline_client.model.spark_job_status import SparkJobStatus
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    body = SparkJobSubmitRequest(
        python_file="python_file_example",
        job_name="job_name_example",
        args="args_example",
        mode="mode_example",
    )
    try:
        # Submit a Spark job
        api_response = api_instance.spark_submit_job(
            body=body,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_submit_job: %s\n" % e)
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
[**SparkJobSubmitRequest**](../../models/SparkJobSubmitRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#spark_submit_job.ApiResponseFor200) | Success.
404 | [ApiResponseFor404](#spark_submit_job.ApiResponseFor404) | A specified resource is not found.
500 | [ApiResponseFor500](#spark_submit_job.ApiResponseFor500) | Unknown server error.

#### spark_submit_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SparkJobStatus**](../../models/SparkJobStatus.md) |  | 


#### spark_submit_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### spark_submit_job.ApiResponseFor500
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

# **spark_submit_sql**
<a id="spark_submit_sql"></a>
> SqlExecuteResponse spark_submit_sql(sql_query)

Submit a Spark SQL job

Submit a Spark job to run a sql query inside a python spark template.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
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
    api_instance = spark_api.SparkApi(api_client)

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
        # Submit a Spark SQL job
        api_response = api_instance.spark_submit_sql(
            body=body,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_submit_sql: %s\n" % e)
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
200 | [ApiResponseFor200](#spark_submit_sql.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#spark_submit_sql.ApiResponseFor500) | Unknown server error.

#### spark_submit_sql.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlExecuteResponse**](../../models/SqlExecuteResponse.md) |  | 


#### spark_submit_sql.ApiResponseFor500
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

# **spark_update_sql**
<a id="spark_update_sql"></a>
> spark_update_sql(file)

Update user Spark SQL query cache

Update user Spark SQL query cache.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import spark_api
from hyperline_client.model.error import Error
from hyperline_client.model.file import File
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
    api_instance = spark_api.SparkApi(api_client)

    # example passing only required values which don't have defaults set
    body = File(
        name="name_example",
        content="content_example",
        path="path_example",
    )
    try:
        # Update user Spark SQL query cache
        api_response = api_instance.spark_update_sql(
            body=body,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling SparkApi->spark_update_sql: %s\n" % e)
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
[**File**](../../models/File.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#spark_update_sql.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#spark_update_sql.ApiResponseFor500) | Unknown server error.

#### spark_update_sql.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### spark_update_sql.ApiResponseFor500
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

