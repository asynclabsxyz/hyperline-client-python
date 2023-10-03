# IntegrationConfigS3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** |  | [optional] 
**access_key_id** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.integration_config_s3 import IntegrationConfigS3

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationConfigS3 from a JSON string
integration_config_s3_instance = IntegrationConfigS3.from_json(json)
# print the JSON string representation of the object
print IntegrationConfigS3.to_json()

# convert the object into a dict
integration_config_s3_dict = integration_config_s3_instance.to_dict()
# create an instance of IntegrationConfigS3 from a dict
integration_config_s3_form_dict = integration_config_s3.from_dict(integration_config_s3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


