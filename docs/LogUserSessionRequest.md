# LogUserSessionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_url** | **str** |  | 

## Example

```python
from hyperline_client.models.log_user_session_request import LogUserSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserSessionRequest from a JSON string
log_user_session_request_instance = LogUserSessionRequest.from_json(json)
# print the JSON string representation of the object
print LogUserSessionRequest.to_json()

# convert the object into a dict
log_user_session_request_dict = log_user_session_request_instance.to_dict()
# create an instance of LogUserSessionRequest from a dict
log_user_session_request_form_dict = log_user_session_request.from_dict(log_user_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


