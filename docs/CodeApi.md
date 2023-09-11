# hyperline_client.CodeApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code_file**](CodeApi.md#create_code_file) | **POST** /code | Create a file
[**list_code_files**](CodeApi.md#list_code_files) | **GET** /code | List code files
[**list_code_samples**](CodeApi.md#list_code_samples) | **GET** /code/samples | List code files


# **create_code_file**
> File create_code_file(file_create_request)

Create a file

Create a file in storage.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.file import File
from hyperline_client.models.file_create_request import FileCreateRequest
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
    api_instance = hyperline_client.CodeApi(api_client)
    file_create_request = hyperline_client.FileCreateRequest() # FileCreateRequest | 

    try:
        # Create a file
        api_response = api_instance.create_code_file(file_create_request)
        print("The response of CodeApi->create_code_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeApi->create_code_file: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_create_request** | [**FileCreateRequest**](FileCreateRequest.md)|  | 

### Return type

[**File**](File.md)

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

# **list_code_files**
> FileCollection list_code_files(folder=folder)

List code files

List code files.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.file_collection import FileCollection
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
    api_instance = hyperline_client.CodeApi(api_client)
    folder = 'folder_example' # str | If set, only return files within this folder. (optional)

    try:
        # List code files
        api_response = api_instance.list_code_files(folder=folder)
        print("The response of CodeApi->list_code_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeApi->list_code_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| If set, only return files within this folder. | [optional] 

### Return type

[**FileCollection**](FileCollection.md)

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

# **list_code_samples**
> SamplesCollection list_code_samples(type=type, tag=tag)

List code files

List code samples.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.samples_collection import SamplesCollection
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
    api_instance = hyperline_client.CodeApi(api_client)
    type = 'type_example' # str | Filter samples to a specific type (SQL, python, ..) (optional)
    tag = 'tag_example' # str | Filter samples to a specific tag (optional)

    try:
        # List code files
        api_response = api_instance.list_code_samples(type=type, tag=tag)
        print("The response of CodeApi->list_code_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeApi->list_code_samples: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter samples to a specific type (SQL, python, ..) | [optional] 
 **tag** | **str**| Filter samples to a specific tag | [optional] 

### Return type

[**SamplesCollection**](SamplesCollection.md)

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

