# hyperline_client.SqlApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_sql_job**](SqlApi.md#check_sql_job) | **GET** /sql/jobs/{job_id}/status | Check the status of a SQL job
[**execute_sql_query**](SqlApi.md#execute_sql_query) | **POST** /sql | Execute a SQL query
[**get_sql_cache**](SqlApi.md#get_sql_cache) | **GET** /sql/edit | Get user SQL query cache
[**get_sql_job_details**](SqlApi.md#get_sql_job_details) | **GET** /sql/jobs/{job_id}/details | Check the status of a SQL job
[**get_sql_job_output**](SqlApi.md#get_sql_job_output) | **GET** /sql/jobs/{job_id}/output | Get the output of a SQL job
[**get_sql_queries**](SqlApi.md#get_sql_queries) | **GET** /sql/queries | Get user SQL queries
[**submit_sql_job**](SqlApi.md#submit_sql_job) | **POST** /sql/jobs | Submit a SQL job
[**update_sql_cache**](SqlApi.md#update_sql_cache) | **POST** /sql/edit | Update user SQL query cache
[**update_sql_query**](SqlApi.md#update_sql_query) | **POST** /sql/queries | Update user SQL query cache


# **check_sql_job**
> SqlJobStatus check_sql_job(job_id)

Check the status of a SQL job

Check the status of a SQL job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_job_status import SqlJobStatus
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
    api_instance = hyperline_client.SqlApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.

    try:
        # Check the status of a SQL job
        api_response = api_instance.check_sql_job(job_id)
        print("The response of SqlApi->check_sql_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->check_sql_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 

### Return type

[**SqlJobStatus**](SqlJobStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | A specified resource is not found. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_sql_query**
> SqlExecuteResponse execute_sql_query(sql_query)

Execute a SQL query

Execute a SQL query.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_execute_response import SqlExecuteResponse
from hyperline_client.models.sql_query import SqlQuery
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
    api_instance = hyperline_client.SqlApi(api_client)
    sql_query = hyperline_client.SqlQuery() # SqlQuery | 

    try:
        # Execute a SQL query
        api_response = api_instance.execute_sql_query(sql_query)
        print("The response of SqlApi->execute_sql_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->execute_sql_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_query** | [**SqlQuery**](SqlQuery.md)|  | 

### Return type

[**SqlExecuteResponse**](SqlExecuteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | A specified resource is not found. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_cache**
> SqlQuery get_sql_cache()

Get user SQL query cache

Get user SQL query cache.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_query import SqlQuery
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
    api_instance = hyperline_client.SqlApi(api_client)

    try:
        # Get user SQL query cache
        api_response = api_instance.get_sql_cache()
        print("The response of SqlApi->get_sql_cache:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->get_sql_cache: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SqlQuery**](SqlQuery.md)

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

# **get_sql_job_details**
> SqlJobDetails get_sql_job_details(job_id, engine)

Check the status of a SQL job

Get runtime details about a job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_job_details import SqlJobDetails
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
    api_instance = hyperline_client.SqlApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.
    engine = 'engine_example' # str | SQL engine this job belongs to.

    try:
        # Check the status of a SQL job
        api_response = api_instance.get_sql_job_details(job_id, engine)
        print("The response of SqlApi->get_sql_job_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->get_sql_job_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 
 **engine** | **str**| SQL engine this job belongs to. | 

### Return type

[**SqlJobDetails**](SqlJobDetails.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | A specified resource is not found. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_job_output**
> SqlExecuteResponse get_sql_job_output(job_id)

Get the output of a SQL job

Get the output of a SQL job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_execute_response import SqlExecuteResponse
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
    api_instance = hyperline_client.SqlApi(api_client)
    job_id = 'job_id_example' # str | The Job ID.

    try:
        # Get the output of a SQL job
        api_response = api_instance.get_sql_job_output(job_id)
        print("The response of SqlApi->get_sql_job_output:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->get_sql_job_output: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The Job ID. | 

### Return type

[**SqlExecuteResponse**](SqlExecuteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | A specified resource is not found. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_queries**
> SqlQueryCollection get_sql_queries()

Get user SQL queries

Get user SQL queries from DB.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_query_collection import SqlQueryCollection
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
    api_instance = hyperline_client.SqlApi(api_client)

    try:
        # Get user SQL queries
        api_response = api_instance.get_sql_queries()
        print("The response of SqlApi->get_sql_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->get_sql_queries: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**SqlQueryCollection**](SqlQueryCollection.md)

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

# **submit_sql_job**
> SqlExecuteResponse submit_sql_job(sql_query)

Submit a SQL job

Submit a SQL job.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_execute_response import SqlExecuteResponse
from hyperline_client.models.sql_query import SqlQuery
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
    api_instance = hyperline_client.SqlApi(api_client)
    sql_query = hyperline_client.SqlQuery() # SqlQuery | 

    try:
        # Submit a SQL job
        api_response = api_instance.submit_sql_job(sql_query)
        print("The response of SqlApi->submit_sql_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->submit_sql_job: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_query** | [**SqlQuery**](SqlQuery.md)|  | 

### Return type

[**SqlExecuteResponse**](SqlExecuteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**404** | A specified resource is not found. |  -  |
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sql_cache**
> update_sql_cache(sql_query)

Update user SQL query cache

Update user SQL query cache.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_query import SqlQuery
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
    api_instance = hyperline_client.SqlApi(api_client)
    sql_query = hyperline_client.SqlQuery() # SqlQuery | 

    try:
        # Update user SQL query cache
        api_instance.update_sql_cache(sql_query)
    except Exception as e:
        print("Exception when calling SqlApi->update_sql_cache: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_query** | [**SqlQuery**](SqlQuery.md)|  | 

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

# **update_sql_query**
> SqlQuery update_sql_query(sql_query)

Update user SQL query cache

Update user SQL query cache.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.sql_query import SqlQuery
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
    api_instance = hyperline_client.SqlApi(api_client)
    sql_query = hyperline_client.SqlQuery() # SqlQuery | 

    try:
        # Update user SQL query cache
        api_response = api_instance.update_sql_query(sql_query)
        print("The response of SqlApi->update_sql_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->update_sql_query: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_query** | [**SqlQuery**](SqlQuery.md)|  | 

### Return type

[**SqlQuery**](SqlQuery.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

