# GcmSignupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt_token** | **str** |  | 
**user_email** | **str** |  | 

## Example

```python
from hyperline_client.models.gcm_signup_request import GcmSignupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GcmSignupRequest from a JSON string
gcm_signup_request_instance = GcmSignupRequest.from_json(json)
# print the JSON string representation of the object
print GcmSignupRequest.to_json()

# convert the object into a dict
gcm_signup_request_dict = gcm_signup_request_instance.to_dict()
# create an instance of GcmSignupRequest from a dict
gcm_signup_request_form_dict = gcm_signup_request.from_dict(gcm_signup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


