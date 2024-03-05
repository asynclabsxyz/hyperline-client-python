# User

A user object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The user&#39;s email | [optional] 
**name** | **str** | The user&#39;s name | 
**organization** | **str** | The user&#39;s organization name | 
**joined** | **datetime** | The datetime the user joined | [optional] [readonly] 
**role** | **str** | The user&#39;s role | 
**secrets** | **str** | The user&#39;s secrets | [optional] 
**status** | **str** | The user&#39;s status | [optional] 
**org_id** | **int** | The user&#39;s org id | [optional] 
**org_workspace_id** | **str** | The user&#39;s org workspace identifier | [optional] 
**impersonated_user** | **str** | The user&#39;s impersonated user | [optional] 

## Example

```python
from hyperline_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


