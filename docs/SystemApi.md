# hyperline_client.SystemApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gcm_signup**](SystemApi.md#gcm_signup) | **POST** /system/gcm/signup | For users coming from Google Marketplace to signup to Hyperline.
[**get_all_usages**](SystemApi.md#get_all_usages) | **GET** /system/usage | Get Usage
[**get_system_usage_details**](SystemApi.md#get_system_usage_details) | **GET** /system/usage/details/{id} | Get Organization Usage Details
[**system_auth**](SystemApi.md#system_auth) | **GET** /system/auth | For Auth0 to verify user is authorized in backend.
[**verify_invitation**](SystemApi.md#verify_invitation) | **POST** /invitation/verify | Verifies an invitation and onboards.


# **gcm_signup**
> gcm_signup(gcm_signup_request)

For users coming from Google Marketplace to signup to Hyperline.

For users to sign up using Google Marketplace.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.gcm_signup_request import GcmSignupRequest
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
    api_instance = hyperline_client.SystemApi(api_client)
    gcm_signup_request = hyperline_client.GcmSignupRequest() # GcmSignupRequest | 

    try:
        # For users coming from Google Marketplace to signup to Hyperline.
        api_instance.gcm_signup(gcm_signup_request)
    except Exception as e:
        print("Exception when calling SystemApi->gcm_signup: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcm_signup_request** | [**GcmSignupRequest**](GcmSignupRequest.md)|  | 

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

# **get_all_usages**
> GetAllUsagesResponse get_all_usages(days=days)

Get Usage

Get Usage for all Organizations

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.get_all_usages_response import GetAllUsagesResponse
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
    api_instance = hyperline_client.SystemApi(api_client)
    days = 56 # int | number of days (optional)

    try:
        # Get Usage
        api_response = api_instance.get_all_usages(days=days)
        print("The response of SystemApi->get_all_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_all_usages: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**| number of days | [optional] 

### Return type

[**GetAllUsagesResponse**](GetAllUsagesResponse.md)

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

# **get_system_usage_details**
> OrgUsageDetails get_system_usage_details(id)

Get Organization Usage Details

Get Organization Usage Details

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.org_usage_details import OrgUsageDetails
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
    api_instance = hyperline_client.SystemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Organization Usage Details
        api_response = api_instance.get_system_usage_details(id)
        print("The response of SystemApi->get_system_usage_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->get_system_usage_details: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrgUsageDetails**](OrgUsageDetails.md)

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

# **system_auth**
> SystemAuthResponse system_auth(email)

For Auth0 to verify user is authorized in backend.

For Auth0 to verify user is authorized in backend.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.system_auth_response import SystemAuthResponse
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
    api_instance = hyperline_client.SystemApi(api_client)
    email = 'email_example' # str | 

    try:
        # For Auth0 to verify user is authorized in backend.
        api_response = api_instance.system_auth(email)
        print("The response of SystemApi->system_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->system_auth: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**SystemAuthResponse**](SystemAuthResponse.md)

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

# **verify_invitation**
> InvitationVerifyResponse verify_invitation(invitation_verify_request)

Verifies an invitation and onboards.

Verifies an invitation and possibly trigger account creation.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.invitation_verify_request import InvitationVerifyRequest
from hyperline_client.models.invitation_verify_response import InvitationVerifyResponse
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
    api_instance = hyperline_client.SystemApi(api_client)
    invitation_verify_request = hyperline_client.InvitationVerifyRequest() # InvitationVerifyRequest | 

    try:
        # Verifies an invitation and onboards.
        api_response = api_instance.verify_invitation(invitation_verify_request)
        print("The response of SystemApi->verify_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->verify_invitation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_verify_request** | [**InvitationVerifyRequest**](InvitationVerifyRequest.md)|  | 

### Return type

[**InvitationVerifyResponse**](InvitationVerifyResponse.md)

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

