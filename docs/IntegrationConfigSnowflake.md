# IntegrationConfigSnowflake


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**account** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**warehouse** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.integration_config_snowflake import IntegrationConfigSnowflake

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigSnowflake from a JSON string
integration_config_snowflake_instance = IntegrationConfigSnowflake.from_json(json)
# print the JSON string representation of the object
print IntegrationConfigSnowflake.to_json()

# convert the object into a dict
integration_config_snowflake_dict = integration_config_snowflake_instance.to_dict()
# create an instance of IntegrationConfigSnowflake from a dict
integration_config_snowflake_form_dict = integration_config_snowflake.from_dict(integration_config_snowflake_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


