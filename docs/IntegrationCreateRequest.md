# IntegrationCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**config** | [**IntegrationCreateRequestConfig**](IntegrationCreateRequestConfig.md) |  | [optional] 

## Example

```python
from hyperline_client.models.integration_create_request import IntegrationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCreateRequest from a JSON string
integration_create_request_instance = IntegrationCreateRequest.from_json(json)
# print the JSON string representation of the object
print IntegrationCreateRequest.to_json()

# convert the object into a dict
integration_create_request_dict = integration_create_request_instance.to_dict()
# create an instance of IntegrationCreateRequest from a dict
integration_create_request_form_dict = integration_create_request.from_dict(integration_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


