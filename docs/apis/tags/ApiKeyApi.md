<a id="__pageTop"></a>
# hyperline_client.apis.tags.api_key_api.ApiKeyApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](#create_api_key) | **post** /api_keys | Create an API key
[**get_api_key**](#get_api_key) | **get** /api_keys | Get an API key info

# **create_api_key**
<a id="create_api_key"></a>
> ApiKey create_api_key()

Create an API key

Create an API key.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import api_key_api
from hyperline_client.model.error import Error
from hyperline_client.model.api_key import ApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create an API key
        api_response = api_instance.create_api_key()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling ApiKeyApi->create_api_key: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_api_key.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#create_api_key.ApiResponseFor500) | Unknown server error.
400 | [ApiResponseFor400](#create_api_key.ApiResponseFor400) | Client specified an invalid argument.

#### create_api_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKey**](../../models/ApiKey.md) |  | 


#### create_api_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_api_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadUserRequest**](../../models/BadUserRequest.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_key**
<a id="get_api_key"></a>
> ApiKey get_api_key()

Get an API key info

Get an API key info.

### Example

* Bearer Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import api_key_api
from hyperline_client.model.error import Error
from hyperline_client.model.api_key import ApiKey
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
    api_instance = api_key_api.ApiKeyApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get an API key info
        api_response = api_instance.get_api_key()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling ApiKeyApi->get_api_key: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_key.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_api_key.ApiResponseFor500) | Unknown server error.
400 | [ApiResponseFor400](#get_api_key.ApiResponseFor400) | Client specified an invalid argument.

#### get_api_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiKey**](../../models/ApiKey.md) |  | 


#### get_api_key.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_api_key.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadUserRequest**](../../models/BadUserRequest.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

