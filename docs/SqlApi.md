# hyperline_client.SqlApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_sql_query**](SqlApi.md#execute_sql_query) | **POST** /sql | Execute a SQL query
[**execute_sql_query_async**](SqlApi.md#execute_sql_query_async) | **POST** /sql/execute | Executes a SQL query async
[**get_sql_job_details**](SqlApi.md#get_sql_job_details) | **GET** /sql/jobs/{job_id}/details | Check the status of a SQL job


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
**500** | Unknown server error. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_sql_query_async**
> SqlExecuteResponse execute_sql_query_async(sql_query)

Executes a SQL query async

Executes a SQL query asynchronously. Client doesn't have to wait for the entire response.

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
        # Executes a SQL query async
        api_response = api_instance.execute_sql_query_async(sql_query)
        print("The response of SqlApi->execute_sql_query_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->execute_sql_query_async: %s\n" % e)
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
**500** | Unknown server error. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

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
**500** | Unknown server error. |  -  |
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

