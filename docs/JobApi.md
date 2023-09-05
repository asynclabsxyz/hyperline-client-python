# hyperline_client.JobApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_jobs**](JobApi.md#list_jobs) | **GET** /jobs | List user jobs


# **list_jobs**
> JobCollection list_jobs(isactive=isactive, type=type, status=status, creator=creator)

List user jobs

List jobs matching the filter.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.job_collection import JobCollection
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
    api_instance = hyperline_client.JobApi(api_client)
    isactive = True # bool | should the job be in active state (optional)
    type = 'type_example' # str | The type of the job/file. (optional)
    status = 'status_example' # str |  (optional)
    creator = 'creator_example' # str | creator of the job (optional)

    try:
        # List user jobs
        api_response = api_instance.list_jobs(isactive=isactive, type=type, status=status, creator=creator)
        print("The response of JobApi->list_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobApi->list_jobs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isactive** | **bool**| should the job be in active state | [optional] 
 **type** | **str**| The type of the job/file. | [optional] 
 **status** | **str**|  | [optional] 
 **creator** | **str**| creator of the job | [optional] 

### Return type

[**JobCollection**](JobCollection.md)

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

