# GetAllUsagesResponse

Response object for system all usages request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usages** | [**List[OrgUsage]**](OrgUsage.md) |  | [optional] 

## Example

```python
from hyperline_client.models.get_all_usages_response import GetAllUsagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllUsagesResponse from a JSON string
get_all_usages_response_instance = GetAllUsagesResponse.from_json(json)
# print the JSON string representation of the object
print GetAllUsagesResponse.to_json()

# convert the object into a dict
get_all_usages_response_dict = get_all_usages_response_instance.to_dict()
# create an instance of GetAllUsagesResponse from a dict
get_all_usages_response_form_dict = get_all_usages_response.from_dict(get_all_usages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


