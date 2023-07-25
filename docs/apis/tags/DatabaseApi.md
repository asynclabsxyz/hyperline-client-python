<a id="__pageTop"></a>
# hyperline_client.apis.tags.database_api.DatabaseApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_schema**](#get_database_schema) | **get** /database/schema | Get database schema

# **get_database_schema**
<a id="get_database_schema"></a>
> SqlSchema get_database_schema()

Get database schema

Get custom database schema.

### Example

* OAuth Authentication (oAuthNoScopes):
* Bearer (JWT) Authentication (bearerAuth):
```python
import hyperline_client
from hyperline_client.apis.tags import database_api
from hyperline_client.model.error import Error
from hyperline_client.model.sql_schema import SqlSchema
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

# Configure OAuth2 access token for authorization: oAuthNoScopes
configuration = hyperline_client.Configuration(
    host = "/api/v1beta",
    access_token = 'YOUR_ACCESS_TOKEN'
)

# Configure Bearer authorization (JWT): bearerAuth
configuration = hyperline_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with hyperline_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = database_api.DatabaseApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get database schema
        api_response = api_instance.get_database_schema()
        pprint(api_response)
    except hyperline_client.ApiException as e:
        print("Exception when calling DatabaseApi->get_database_schema: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_database_schema.ApiResponseFor200) | Success.
500 | [ApiResponseFor500](#get_database_schema.ApiResponseFor500) | Unknown server error.

#### get_database_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SqlSchema**](../../models/SqlSchema.md) |  | 


#### get_database_schema.ApiResponseFor500
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

[oAuthNoScopes](../../../README.md#oAuthNoScopes), [bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

