# StageInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | 
**run_id** | **str** |  | 
**stage_name** | **str** |  | 
**execution_date** | **date** |  | [optional] 
**duration** | **float** |  | 
**state** | **str** |  | 
**try_number** | **int** |  | 

## Example

```python
from hyperline_client.models.stage_instance import StageInstance

# TODO update the JSON string below
json = "{}"
# create an instance of StageInstance from a JSON string
stage_instance_instance = StageInstance.from_json(json)
# print the JSON string representation of the object
print StageInstance.to_json()

# convert the object into a dict
stage_instance_dict = stage_instance_instance.to_dict()
# create an instance of StageInstance from a dict
stage_instance_form_dict = stage_instance.from_dict(stage_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


