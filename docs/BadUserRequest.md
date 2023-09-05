# BadUserRequest

Unable to process request successfully due to input error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bad_request** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 

## Example

```python
from hyperline_client.models.bad_user_request import BadUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BadUserRequest from a JSON string
bad_user_request_instance = BadUserRequest.from_json(json)
# print the JSON string representation of the object
print BadUserRequest.to_json()

# convert the object into a dict
bad_user_request_dict = bad_user_request_instance.to_dict()
# create an instance of BadUserRequest from a dict
bad_user_request_form_dict = bad_user_request.from_dict(bad_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


