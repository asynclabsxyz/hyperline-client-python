# IntegrationCreateRequestConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | [optional] 
**service_account_key_json** | **str** |  | [optional] 
**access_key_id** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**tcp_host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.integration_create_request_config import IntegrationCreateRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationCreateRequestConfig from a JSON string
integration_create_request_config_instance = IntegrationCreateRequestConfig.from_json(json)
# print the JSON string representation of the object
print IntegrationCreateRequestConfig.to_json()

# convert the object into a dict
integration_create_request_config_dict = integration_create_request_config_instance.to_dict()
# create an instance of IntegrationCreateRequestConfig from a dict
integration_create_request_config_form_dict = integration_create_request_config.from_dict(integration_create_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


