# IntegrationConfigGCS


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | [optional] 
**service_account_key_json** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.integration_config_gcs import IntegrationConfigGCS

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigGCS from a JSON string
integration_config_gcs_instance = IntegrationConfigGCS.from_json(json)
# print the JSON string representation of the object
print IntegrationConfigGCS.to_json()

# convert the object into a dict
integration_config_gcs_dict = integration_config_gcs_instance.to_dict()
# create an instance of IntegrationConfigGCS from a dict
integration_config_gcs_form_dict = integration_config_gcs.from_dict(integration_config_gcs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


