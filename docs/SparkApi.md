# hyperline_client.SparkApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spark_cancel_job**](SparkApi.md#spark_cancel_job) | **POST** /spark/{job_id}/cancel | Cancel a Spark job
[**spark_check_job**](SparkApi.md#spark_check_job) | **GET** /spark/{job_id} | Check a Spark job status
[**spark_get_job_output**](SparkApi.md#spark_get_job_output) | **GET** /spark/{job_id}/output | Get Spark job output
[**spark_list_jobs**](SparkApi.md#spark_list_jobs) | **GET** /spark | List Spark jobs
[**spark_list_saved_jobs**](SparkApi.md#spark_list_saved_jobs) | **GET** /spark/jobs/saved | List saved spark jobs
[**spark_save_job**](SparkApi.md#spark_save_job) | **POST** /spark/{job_id}/save | Save a spark job for pipeline
[**spark_submit_job**](SparkApi.md#spark_submit_job) | **POST** /spark | Submit a Spark job


# **spark_cancel_job**
> SparkJobStatus spark_cancel_job(job_id)

Cancel a Spark job

Cancel a Spark job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_status import SparkJobStatus
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
    api_instance = hyperline_client.SparkApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.

    try:
        # Cancel a Spark job
        api_response = api_instance.spark_cancel_job(job_id)
        print("The response of SparkApi->spark_cancel_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_cancel_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 

### Return type

[**SparkJobStatus**](SparkJobStatus.md)

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_check_job**
> SparkJobStatus spark_check_job(job_id)

Check a Spark job status

Check the status of a Spark job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_status import SparkJobStatus
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
    api_instance = hyperline_client.SparkApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.

    try:
        # Check a Spark job status
        api_response = api_instance.spark_check_job(job_id)
        print("The response of SparkApi->spark_check_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_check_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 

### Return type

[**SparkJobStatus**](SparkJobStatus.md)

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_get_job_output**
> SparkJobOutput spark_get_job_output(job_id)

Get Spark job output

Get output data from a Spark job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_output import SparkJobOutput
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
    api_instance = hyperline_client.SparkApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.

    try:
        # Get Spark job output
        api_response = api_instance.spark_get_job_output(job_id)
        print("The response of SparkApi->spark_get_job_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_get_job_output: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 

### Return type

[**SparkJobOutput**](SparkJobOutput.md)

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_list_jobs**
> SparkJobCollection spark_list_jobs()

List Spark jobs

List Spark jobs.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_collection import SparkJobCollection
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
    api_instance = hyperline_client.SparkApi(api_client)

    try:
        # List Spark jobs
        api_response = api_instance.spark_list_jobs()
        print("The response of SparkApi->spark_list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_list_jobs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SparkJobCollection**](SparkJobCollection.md)

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_list_saved_jobs**
> SavedJobCollection spark_list_saved_jobs()

List saved spark jobs

List saved spark jobs.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.saved_job_collection import SavedJobCollection
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
    api_instance = hyperline_client.SparkApi(api_client)

    try:
        # List saved spark jobs
        api_response = api_instance.spark_list_saved_jobs()
        print("The response of SparkApi->spark_list_saved_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_list_saved_jobs: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SavedJobCollection**](SavedJobCollection.md)

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_save_job**
> spark_save_job(job_id, spark_job_save_request)

Save a spark job for pipeline

Save a spark job to pipeline jobs directory.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_save_request import SparkJobSaveRequest
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
    api_instance = hyperline_client.SparkApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.
    spark_job_save_request = hyperline_client.SparkJobSaveRequest() # SparkJobSaveRequest | 

    try:
        # Save a spark job for pipeline
        api_instance.spark_save_job(job_id, spark_job_save_request)
    except Exception as e:
        print("Exception when calling SparkApi->spark_save_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 
 **spark_job_save_request** | [**SparkJobSaveRequest**](SparkJobSaveRequest.md)|  | 

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spark_submit_job**
> SparkJobStatus spark_submit_job(spark_job_submit_request)

Submit a Spark job

Submit a Spark job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.spark_job_status import SparkJobStatus
from hyperline_client.models.spark_job_submit_request import SparkJobSubmitRequest
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
    api_instance = hyperline_client.SparkApi(api_client)
    spark_job_submit_request = hyperline_client.SparkJobSubmitRequest() # SparkJobSubmitRequest | 

    try:
        # Submit a Spark job
        api_response = api_instance.spark_submit_job(spark_job_submit_request)
        print("The response of SparkApi->spark_submit_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SparkApi->spark_submit_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spark_job_submit_request** | [**SparkJobSubmitRequest**](SparkJobSubmitRequest.md)|  | 

### Return type

[**SparkJobStatus**](SparkJobStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**500** | Unknown server error. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

