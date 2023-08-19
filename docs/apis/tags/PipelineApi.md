<a id="__pageTop"></a>
# hyperline_client.apis.tags.pipeline_api.PipelineApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backfill_pipeline**](#backfill_pipeline) | **post** /pipeline/backfill | Backfill a pipeline
[**create_pipeline**](#create_pipeline) | **post** /pipelines | Create a pipeline
[**delete_pipeline**](#delete_pipeline) | **post** /pipelines/{pipeline_name}/delete | Delete a pipeline
[**deploy_pipeline**](#deploy_pipeline) | **post** /pipelines/{pipeline_name}/deploy | Deploy a pipeline
[**edit_pipeline**](#edit_pipeline) | **post** /pipeline/edit | Edit a pipeline
[**get_pipeline**](#get_pipeline) | **get** /pipelines/{pipeline_name} | Get a pipeline
[**get_pipeline_run**](#get_pipeline_run) | **get** /pipelines/{pipeline_name}/runs/{run_id} | Get information of a pipeline run
[**get_stage_instances**](#get_stage_instances) | **get** /pipelines/{pipeline_name}/runs/{run_id}/stages | Get stage instances of a pipeline
[**get_stage_log**](#get_stage_log) | **get** /pipelines/{pipeline_name}/runs/{run_id}/stages/{stage_name}/logs/{try_number} | Get the logs of a pipeline stage instance
[**list_pipeline_runs**](#list_pipeline_runs) | **get** /pipelines/{pipeline_name}/runs | List runs of a pipeline
[**list_pipelines**](#list_pipelines) | **get** /pipelines | List pipelines
[**pause_pipeline**](#pause_pipeline) | **post** /pipelines/{pipeline_name}/pause | Pause a pipeline
[**trigger_pipeline**](#trigger_pipeline) | **post** /pipelines/{pipeline_name}/trigger | Delete a pipeline

# **backfill_pipeline**
<a id="backfill_pipeline"></a>
> backfill_pipeline(pipeline_backfill_request)

Backfill a pipeline

Backfill a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.pipeline_backfill_request import PipelineBackfillRequest
from hyperline_client.model.error import Error
from hyperline_client.model.bad_user_request import BadUserRequest
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    body = PipelineBackfillRequest(
        pipeline_name="pipeline_name_example",
        argument_name="argument_name_example",
        start_date="1970-01-01",
        end_date="1970-01-01",
        interval=1,
    )
    try:
        # Backfill a pipeline
        api_response = api_instance.backfill_pipeline(
            body=body,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->backfill_pipeline: %s\n" % e)
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
[**PipelineBackfillRequest**](../../models/PipelineBackfillRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#backfill_pipeline.ApiResponseFor204) | Success.
400 | [ApiResponseFor400](#backfill_pipeline.ApiResponseFor400) | Client specified an invalid argument.
500 | [ApiResponseFor500](#backfill_pipeline.ApiResponseFor500) | Unknown server error.

#### backfill_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### backfill_pipeline.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadUserRequest**](../../models/BadUserRequest.md) |  | 


#### backfill_pipeline.ApiResponseFor500
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

# **create_pipeline**
<a id="create_pipeline"></a>
> create_pipeline(pipeline)

Create a pipeline

Create a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline import Pipeline
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    body = Pipeline(
        pipeline_name="pipeline_name_example",
        schedule="schedule_example",
        stages=[
            Stage(
                stage_name="stage_name_example",
                job_type="job_type_example",
                job_name="job_name_example",
                arguments="arguments_example",
                package="package_example",
            )
        ],
        max_active_runs=1,
        retries=1,
null,
        catchup=True,
        write_test_mode=True,
        sample_reads=True,
    )
    try:
        # Create a pipeline
        api_response = api_instance.create_pipeline(
            body=body,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->create_pipeline: %s\n" % e)
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
[**Pipeline**](../../models/Pipeline.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_pipeline.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#create_pipeline.ApiResponseFor500) | Unknown server error.

#### create_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_pipeline.ApiResponseFor500
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

# **delete_pipeline**
<a id="delete_pipeline"></a>
> delete_pipeline(pipeline_name)

Delete a pipeline

Delete a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # Delete a pipeline
        api_response = api_instance.delete_pipeline(
            path_params=path_params,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->delete_pipeline: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_pipeline.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#delete_pipeline.ApiResponseFor500) | Unknown server error.

#### delete_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_pipeline.ApiResponseFor500
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

# **deploy_pipeline**
<a id="deploy_pipeline"></a>
> deploy_pipeline(pipeline_name)

Deploy a pipeline

Deploy a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # Deploy a pipeline
        api_response = api_instance.deploy_pipeline(
            path_params=path_params,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->deploy_pipeline: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#deploy_pipeline.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#deploy_pipeline.ApiResponseFor500) | Unknown server error.

#### deploy_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### deploy_pipeline.ApiResponseFor500
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

# **edit_pipeline**
<a id="edit_pipeline"></a>
> edit_pipeline(pipeline)

Edit a pipeline

Edit a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline import Pipeline
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    body = Pipeline(
        pipeline_name="pipeline_name_example",
        schedule="schedule_example",
        stages=[
            Stage(
                stage_name="stage_name_example",
                job_type="job_type_example",
                job_name="job_name_example",
                arguments="arguments_example",
                package="package_example",
            )
        ],
        max_active_runs=1,
        retries=1,
null,
        catchup=True,
        write_test_mode=True,
        sample_reads=True,
    )
    try:
        # Edit a pipeline
        api_response = api_instance.edit_pipeline(
            body=body,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->edit_pipeline: %s\n" % e)
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
[**Pipeline**](../../models/Pipeline.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#edit_pipeline.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#edit_pipeline.ApiResponseFor500) | Unknown server error.

#### edit_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### edit_pipeline.ApiResponseFor500
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

# **get_pipeline**
<a id="get_pipeline"></a>
> Pipeline get_pipeline(pipeline_name)

Get a pipeline

Get information a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline import Pipeline
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # Get a pipeline
        api_response = api_instance.get_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pipeline.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_pipeline.ApiResponseFor500) | Unknown server error.

#### get_pipeline.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Pipeline**](../../models/Pipeline.md) |  | 


#### get_pipeline.ApiResponseFor500
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

# **get_pipeline_run**
<a id="get_pipeline_run"></a>
> PipelineRun get_pipeline_run(pipeline_namerun_id)

Get information of a pipeline run

Get information of a pipeline run.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline_run import PipelineRun
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
        'run_id': "run_id_example",
    }
    try:
        # Get information of a pipeline run
        api_response = api_instance.get_pipeline_run(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->get_pipeline_run: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 
run_id | RunIdSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pipeline_run.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_pipeline_run.ApiResponseFor500) | Unknown server error.

#### get_pipeline_run.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineRun**](../../models/PipelineRun.md) |  | 


#### get_pipeline_run.ApiResponseFor500
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

# **get_stage_instances**
<a id="get_stage_instances"></a>
> StageInstanceCollection get_stage_instances(pipeline_namerun_id)

Get stage instances of a pipeline

Get stage instances of a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.stage_instance_collection import StageInstanceCollection
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
        'run_id': "run_id_example",
    }
    try:
        # Get stage instances of a pipeline
        api_response = api_instance.get_stage_instances(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->get_stage_instances: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 
run_id | RunIdSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stage_instances.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_stage_instances.ApiResponseFor500) | Unknown server error.

#### get_stage_instances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StageInstanceCollection**](../../models/StageInstanceCollection.md) |  | 


#### get_stage_instances.ApiResponseFor500
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

# **get_stage_log**
<a id="get_stage_log"></a>
> File get_stage_log(pipeline_namerun_idstage_nametry_number)

Get the logs of a pipeline stage instance

Get the logs of a pipeline stage instance.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
        'run_id': "run_id_example",
        'stage_name': "stage_name_example",
        'try_number': 1,
    }
    try:
        # Get the logs of a pipeline stage instance
        api_response = api_instance.get_stage_log(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->get_stage_log: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 
run_id | RunIdSchema | | 
stage_name | StageNameSchema | | 
try_number | TryNumberSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RunIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StageNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TryNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_stage_log.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_stage_log.ApiResponseFor500) | Unknown server error.

#### get_stage_log.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**File**](../../models/File.md) |  | 


#### get_stage_log.ApiResponseFor500
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

# **list_pipeline_runs**
<a id="list_pipeline_runs"></a>
> PipelineRunCollection list_pipeline_runs(pipeline_name)

List runs of a pipeline

List runs of a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.pipeline_run_collection import PipelineRunCollection
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # List runs of a pipeline
        api_response = api_instance.list_pipeline_runs(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->list_pipeline_runs: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_pipeline_runs.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_pipeline_runs.ApiResponseFor500) | Unknown server error.

#### list_pipeline_runs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineRunCollection**](../../models/PipelineRunCollection.md) |  | 


#### list_pipeline_runs.ApiResponseFor500
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

# **list_pipelines**
<a id="list_pipelines"></a>
> PipelineMetadataCollection list_pipelines()

List pipelines

List all pipelines created by user's organization.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline_metadata_collection import PipelineMetadataCollection
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List pipelines
        api_response = api_instance.list_pipelines()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->list_pipelines: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_pipelines.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#list_pipelines.ApiResponseFor500) | Unknown server error.

#### list_pipelines.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineMetadataCollection**](../../models/PipelineMetadataCollection.md) |  | 


#### list_pipelines.ApiResponseFor500
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

# **pause_pipeline**
<a id="pause_pipeline"></a>
> pause_pipeline(pipeline_name)

Pause a pipeline

Pause a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
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

# Configure Bearer authorization: bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # Pause a pipeline
        api_response = api_instance.pause_pipeline(
            path_params=path_params,
        )
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->pause_pipeline: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#pause_pipeline.ApiResponseFor204) | Success.
500 | [ApiResponseFor500](#pause_pipeline.ApiResponseFor500) | Unknown server error.

#### pause_pipeline.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### pause_pipeline.ApiResponseFor500
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

# **trigger_pipeline**
<a id="trigger_pipeline"></a>
> PipelineRun trigger_pipeline(pipeline_name)

Delete a pipeline

Trigger a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import pipeline_api
from hyperline_client.model.error import Error
from hyperline_client.model.pipeline_run import PipelineRun
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
    api_instance = pipeline_api.PipelineApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'pipeline_name': "pipeline_name_example",
    }
    try:
        # Delete a pipeline
        api_response = api_instance.trigger_pipeline(
            path_params=path_params,
        )
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling PipelineApi->trigger_pipeline: %s\n" % e)
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
pipeline_name | PipelineNameSchema | | 

# PipelineNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#trigger_pipeline.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#trigger_pipeline.ApiResponseFor500) | Unknown server error.

#### trigger_pipeline.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PipelineRun**](../../models/PipelineRun.md) |  | 


#### trigger_pipeline.ApiResponseFor500
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

