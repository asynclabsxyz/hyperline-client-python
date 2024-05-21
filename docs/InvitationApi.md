# hyperline_client.InvitationApi

All URIs are relative to */api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_invitation**](InvitationApi.md#verify_invitation) | **POST** /invitation/verify | Verifies an invitation and onboards.


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
    api_instance = hyperline_client.InvitationApi(api_client)
    invitation_verify_request = hyperline_client.InvitationVerifyRequest() # InvitationVerifyRequest | 

    try:
        # Verifies an invitation and onboards.
        api_response = api_instance.verify_invitation(invitation_verify_request)
        print("The response of InvitationApi->verify_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationApi->verify_invitation: %s\n" % e)
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

