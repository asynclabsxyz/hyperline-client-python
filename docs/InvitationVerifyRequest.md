# InvitationVerifyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**email** | **str** |  | 

## Example

```python
from hyperline_client.models.invitation_verify_request import InvitationVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationVerifyRequest from a JSON string
invitation_verify_request_instance = InvitationVerifyRequest.from_json(json)
# print the JSON string representation of the object
print InvitationVerifyRequest.to_json()

# convert the object into a dict
invitation_verify_request_dict = invitation_verify_request_instance.to_dict()
# create an instance of InvitationVerifyRequest from a dict
invitation_verify_request_form_dict = invitation_verify_request.from_dict(invitation_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


