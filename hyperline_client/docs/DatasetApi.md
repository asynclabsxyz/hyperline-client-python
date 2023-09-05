# hyperline_client.DatasetApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dataset_metadata**](DatasetApi.md#get_dataset_metadata) | **GET** /datasets/metadata | Get dataset metadata
[**get_dataset_preview**](DatasetApi.md#get_dataset_preview) | **GET** /datasets/preview | Get dataset preview
[**list_datasets**](DatasetApi.md#list_datasets) | **GET** /datasets | List datasets
[**list_explorer_datasets**](DatasetApi.md#list_explorer_datasets) | **GET** /datasets/explorer | List datasets for web explorer
[**list_explorer_datasets_details**](DatasetApi.md#list_explorer_datasets_details) | **GET** /datasets/explorer/details | List datasets details for web explorer


# **get_dataset_metadata**
> object get_dataset_metadata(path, service)

Get dataset metadata

Get dataset metadata.

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
    api_instance = hyperline_client.DatasetApi(api_client)
    path = 'path_example' # str | The path of the file/dataset.
    service = 'service_example' # str | 

    try:
        # Get dataset metadata
        api_response = api_instance.get_dataset_metadata(path, service)
        print("The response of DatasetApi->get_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the file/dataset. | 
 **service** | **str**|  | 

### Return type

**object**

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

# **get_dataset_preview**
> SqlExecuteResponse get_dataset_preview(path, service)

Get dataset preview

Get dataset preview.

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
    api_instance = hyperline_client.DatasetApi(api_client)
    path = 'path_example' # str | The path of the file/dataset.
    service = 'service_example' # str | 

    try:
        # Get dataset preview
        api_response = api_instance.get_dataset_preview(path, service)
        print("The response of DatasetApi->get_dataset_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->get_dataset_preview: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the file/dataset. | 
 **service** | **str**|  | 

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
**500** | Unknown server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datasets**
> DatasetCollection list_datasets()

List datasets

List datasets

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.dataset_collection import DatasetCollection
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
    api_instance = hyperline_client.DatasetApi(api_client)

    try:
        # List datasets
        api_response = api_instance.list_datasets()
        print("The response of DatasetApi->list_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_datasets: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetCollection**](DatasetCollection.md)

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

# **list_explorer_datasets**
> ExplorerViewDatasetCollection list_explorer_datasets()

List datasets for web explorer

List datasets for web explorer.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.explorer_view_dataset_collection import ExplorerViewDatasetCollection
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
    api_instance = hyperline_client.DatasetApi(api_client)

    try:
        # List datasets for web explorer
        api_response = api_instance.list_explorer_datasets()
        print("The response of DatasetApi->list_explorer_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_explorer_datasets: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ExplorerViewDatasetCollection**](ExplorerViewDatasetCollection.md)

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

# **list_explorer_datasets_details**
> ExplorerViewDatasetCollection list_explorer_datasets_details(path)

List datasets details for web explorer

List datasets details for web explorer.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.explorer_view_dataset_collection import ExplorerViewDatasetCollection
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
    api_instance = hyperline_client.DatasetApi(api_client)
    path = 'path_example' # str | The path of the file/dataset.

    try:
        # List datasets details for web explorer
        api_response = api_instance.list_explorer_datasets_details(path)
        print("The response of DatasetApi->list_explorer_datasets_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetApi->list_explorer_datasets_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The path of the file/dataset. | 

### Return type

[**ExplorerViewDatasetCollection**](ExplorerViewDatasetCollection.md)

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

