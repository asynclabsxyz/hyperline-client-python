# hyperline_client.UserApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /user | Create a user
[**get_user**](UserApi.md#get_user) | **GET** /user | Get user info
[**log_session**](UserApi.md#log_session) | **POST** /user/log_session | Logs that the user has started a new session.
[**mark_onboarding_step_complete**](UserApi.md#mark_onboarding_step_complete) | **POST** /user/onboarding | Marks an onboarding step complete for a user
[**mark_tour_finished**](UserApi.md#mark_tour_finished) | **POST** /user/tour | Marks onboard tour for a user


# **create_user**
> User create_user(user)

Create a user

Create a new user with unique email.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.user import User
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
    api_instance = hyperline_client.UserApi(api_client)
    user = hyperline_client.User() # User | 

    try:
        # Create a user
        api_response = api_instance.create_user(user)
        print("The response of UserApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

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

# **get_user**
> User get_user()

Get user info

Get a user info from email.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.user import User
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
    api_instance = hyperline_client.UserApi(api_client)

    try:
        # Get user info
        api_response = api_instance.get_user()
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **log_session**
> log_session(log_user_session_request)

Logs that the user has started a new session.

Logs that the user has started a new session.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.log_user_session_request import LogUserSessionRequest
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
    api_instance = hyperline_client.UserApi(api_client)
    log_user_session_request = hyperline_client.LogUserSessionRequest() # LogUserSessionRequest | 

    try:
        # Logs that the user has started a new session.
        api_instance.log_session(log_user_session_request)
    except Exception as e:
        print("Exception when calling UserApi->log_session: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_user_session_request** | [**LogUserSessionRequest**](LogUserSessionRequest.md)|  | 

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

# **mark_onboarding_step_complete**
> mark_onboarding_step_complete(mark_onboarding_step_request)

Marks an onboarding step complete for a user

Marks that the user has completed an onboarding step.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import hyperline_client
from hyperline_client.models.mark_onboarding_step_request import MarkOnboardingStepRequest
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
    api_instance = hyperline_client.UserApi(api_client)
    mark_onboarding_step_request = hyperline_client.MarkOnboardingStepRequest() # MarkOnboardingStepRequest | 

    try:
        # Marks an onboarding step complete for a user
        api_instance.mark_onboarding_step_complete(mark_onboarding_step_request)
    except Exception as e:
        print("Exception when calling UserApi->mark_onboarding_step_complete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_onboarding_step_request** | [**MarkOnboardingStepRequest**](MarkOnboardingStepRequest.md)|  | 

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

# **mark_tour_finished**
> mark_tour_finished()

Marks onboard tour for a user

Marks that the user has finished the onboarding tour.

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
    api_instance = hyperline_client.UserApi(api_client)

    try:
        # Marks onboard tour for a user
        api_instance.mark_tour_finished()
    except Exception as e:
        print("Exception when calling UserApi->mark_tour_finished: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**400** | Client specified an invalid argument. |  -  |
**401** | Request not authenticated due to missing, invalid, authentication info. |  -  |
**403** | Client does not have sufficient permission. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

