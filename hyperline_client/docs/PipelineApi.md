# hyperline_client.PipelineApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backfill_pipeline**](PipelineApi.md#backfill_pipeline) | **POST** /pipeline/backfill | Backfill a pipeline
[**create_pipeline**](PipelineApi.md#create_pipeline) | **POST** /pipelines | Create a pipeline
[**delete_pipeline**](PipelineApi.md#delete_pipeline) | **POST** /pipelines/{pipeline_name}/delete | Delete a pipeline
[**deploy_pipeline**](PipelineApi.md#deploy_pipeline) | **POST** /pipelines/{pipeline_name}/deploy | Deploy a pipeline
[**edit_pipeline**](PipelineApi.md#edit_pipeline) | **POST** /pipeline/edit | Edit a pipeline
[**get_pipeline**](PipelineApi.md#get_pipeline) | **GET** /pipelines/{pipeline_name} | Get a pipeline
[**get_pipeline_run**](PipelineApi.md#get_pipeline_run) | **GET** /pipelines/{pipeline_name}/runs/{run_id} | Get information of a pipeline run
[**get_stage_instances**](PipelineApi.md#get_stage_instances) | **GET** /pipelines/{pipeline_name}/runs/{run_id}/stages | Get stage instances of a pipeline
[**get_stage_log**](PipelineApi.md#get_stage_log) | **GET** /pipelines/{pipeline_name}/runs/{run_id}/stages/{stage_name}/logs/{try_number} | Get the logs of a pipeline stage instance
[**list_pipeline_runs**](PipelineApi.md#list_pipeline_runs) | **GET** /pipelines/{pipeline_name}/runs | List runs of a pipeline
[**list_pipelines**](PipelineApi.md#list_pipelines) | **GET** /pipelines | List pipelines
[**pause_pipeline**](PipelineApi.md#pause_pipeline) | **POST** /pipelines/{pipeline_name}/pause | Pause a pipeline
[**trigger_pipeline**](PipelineApi.md#trigger_pipeline) | **POST** /pipelines/{pipeline_name}/trigger | Delete a pipeline


# **backfill_pipeline**
> backfill_pipeline(pipeline_backfill_request)

Backfill a pipeline

Backfill a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline_backfill_request import PipelineBackfillRequest
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_backfill_request = hyperline_client.PipelineBackfillRequest() # PipelineBackfillRequest | 

    try:
        # Backfill a pipeline
        api_instance.backfill_pipeline(pipeline_backfill_request)
    except Exception as e:
        print("Exception when calling PipelineApi->backfill_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_backfill_request** | [**PipelineBackfillRequest**](PipelineBackfillRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**400** | Client specified an invalid argument. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pipeline**
> create_pipeline(pipeline)

Create a pipeline

Create a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline import Pipeline
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline = hyperline_client.Pipeline() # Pipeline | 

    try:
        # Create a pipeline
        api_instance.create_pipeline(pipeline)
    except Exception as e:
        print("Exception when calling PipelineApi->create_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**Pipeline**](Pipeline.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pipeline**
> delete_pipeline(pipeline_name)

Delete a pipeline

Delete a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # Delete a pipeline
        api_instance.delete_pipeline(pipeline_name)
    except Exception as e:
        print("Exception when calling PipelineApi->delete_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_pipeline**
> deploy_pipeline(pipeline_name)

Deploy a pipeline

Deploy a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # Deploy a pipeline
        api_instance.deploy_pipeline(pipeline_name)
    except Exception as e:
        print("Exception when calling PipelineApi->deploy_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pipeline**
> edit_pipeline(pipeline)

Edit a pipeline

Edit a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline import Pipeline
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline = hyperline_client.Pipeline() # Pipeline | 

    try:
        # Edit a pipeline
        api_instance.edit_pipeline(pipeline)
    except Exception as e:
        print("Exception when calling PipelineApi->edit_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline** | [**Pipeline**](Pipeline.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline**
> Pipeline get_pipeline(pipeline_name)

Get a pipeline

Get information a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline import Pipeline
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # Get a pipeline
        api_response = api_instance.get_pipeline(pipeline_name)
        print("The response of PipelineApi->get_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

[**Pipeline**](Pipeline.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_run**
> PipelineRun get_pipeline_run(pipeline_name, run_id)

Get information of a pipeline run

Get information of a pipeline run.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline_run import PipelineRun
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.
    run_id = 'run_id_example' # str | The ID of a pipeline run.

    try:
        # Get information of a pipeline run
        api_response = api_instance.get_pipeline_run(pipeline_name, run_id)
        print("The response of PipelineApi->get_pipeline_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_pipeline_run: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 
 **run_id** | **str**| The ID of a pipeline run. | 

### Return type

[**PipelineRun**](PipelineRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stage_instances**
> StageInstanceCollection get_stage_instances(pipeline_name, run_id)

Get stage instances of a pipeline

Get stage instances of a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.stage_instance_collection import StageInstanceCollection
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.
    run_id = 'run_id_example' # str | The ID of a pipeline run.

    try:
        # Get stage instances of a pipeline
        api_response = api_instance.get_stage_instances(pipeline_name, run_id)
        print("The response of PipelineApi->get_stage_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_stage_instances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 
 **run_id** | **str**| The ID of a pipeline run. | 

### Return type

[**StageInstanceCollection**](StageInstanceCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stage_log**
> File get_stage_log(pipeline_name, run_id, stage_name, try_number)

Get the logs of a pipeline stage instance

Get the logs of a pipeline stage instance.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.file import File
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.
    run_id = 'run_id_example' # str | The ID of a pipeline run.
    stage_name = 'stage_name_example' # str | The name of a pipeline stage.
    try_number = 56 # int | The try number of the logs of a pipeline stage instance.

    try:
        # Get the logs of a pipeline stage instance
        api_response = api_instance.get_stage_log(pipeline_name, run_id, stage_name, try_number)
        print("The response of PipelineApi->get_stage_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->get_stage_log: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 
 **run_id** | **str**| The ID of a pipeline run. | 
 **stage_name** | **str**| The name of a pipeline stage. | 
 **try_number** | **int**| The try number of the logs of a pipeline stage instance. | 

### Return type

[**File**](File.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipeline_runs**
> PipelineRunCollection list_pipeline_runs(pipeline_name)

List runs of a pipeline

List runs of a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline_run_collection import PipelineRunCollection
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # List runs of a pipeline
        api_response = api_instance.list_pipeline_runs(pipeline_name)
        print("The response of PipelineApi->list_pipeline_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->list_pipeline_runs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

[**PipelineRunCollection**](PipelineRunCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pipelines**
> PipelineMetadataCollection list_pipelines()

List pipelines

List all pipelines created by user's organization.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline_metadata_collection import PipelineMetadataCollection
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)

    try:
        # List pipelines
        api_response = api_instance.list_pipelines()
        print("The response of PipelineApi->list_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->list_pipelines: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PipelineMetadataCollection**](PipelineMetadataCollection.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause_pipeline**
> pause_pipeline(pipeline_name)

Pause a pipeline

Pause a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # Pause a pipeline
        api_instance.pause_pipeline(pipeline_name)
    except Exception as e:
        print("Exception when calling PipelineApi->pause_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_pipeline**
> PipelineRun trigger_pipeline(pipeline_name)

Delete a pipeline

Trigger a pipeline.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.pipeline_run import PipelineRun
from hyperline_client.rest import ApiException
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
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hyperline_client.PipelineApi(api_client)
    pipeline_name = 'pipeline_name_example' # str | The pipeline name.

    try:
        # Delete a pipeline
        api_response = api_instance.trigger_pipeline(pipeline_name)
        print("The response of PipelineApi->trigger_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelineApi->trigger_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pipeline_name** | **str**| The pipeline name. | 

### Return type

[**PipelineRun**](PipelineRun.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

