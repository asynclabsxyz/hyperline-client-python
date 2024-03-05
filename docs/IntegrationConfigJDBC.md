# IntegrationConfigJDBC


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**tcp_host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.integration_config_jdbc import IntegrationConfigJDBC

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigJDBC from a JSON string
integration_config_jdbc_instance = IntegrationConfigJDBC.from_json(json)
# print the JSON string representation of the object
print IntegrationConfigJDBC.to_json()

# convert the object into a dict
integration_config_jdbc_dict = integration_config_jdbc_instance.to_dict()
# create an instance of IntegrationConfigJDBC from a dict
integration_config_jdbc_form_dict = integration_config_jdbc.from_dict(integration_config_jdbc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


