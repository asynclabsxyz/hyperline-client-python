# InvitationVerifyResponse

Response object for invitation verification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [readonly] 

## Example

```python
from hyperline_client.models.invitation_verify_response import InvitationVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationVerifyResponse from a JSON string
invitation_verify_response_instance = InvitationVerifyResponse.from_json(json)
# print the JSON string representation of the object
print InvitationVerifyResponse.to_json()

# convert the object into a dict
invitation_verify_response_dict = invitation_verify_response_instance.to_dict()
# create an instance of InvitationVerifyResponse from a dict
invitation_verify_response_form_dict = invitation_verify_response.from_dict(invitation_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


