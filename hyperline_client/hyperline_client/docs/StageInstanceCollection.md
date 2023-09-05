# StageInstanceCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stage_instances** | [**List[StageInstance]**](StageInstance.md) |  | [optional] 

## Example

```python
from hyperline_client.models.stage_instance_collection import StageInstanceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of StageInstanceCollection from a JSON string
stage_instance_collection_instance = StageInstanceCollection.from_json(json)
# print the JSON string representation of the object
print StageInstanceCollection.to_json()

# convert the object into a dict
stage_instance_collection_dict = stage_instance_collection_instance.to_dict()
# create an instance of StageInstanceCollection from a dict
stage_instance_collection_form_dict = stage_instance_collection.from_dict(stage_instance_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


