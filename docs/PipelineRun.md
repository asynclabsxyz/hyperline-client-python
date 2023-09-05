# PipelineRun

A run of a pipeline.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | 
**run_id** | **str** |  | 
**state** | **str** |  | [optional] 
**logical_date** | **datetime** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_run import PipelineRun

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRun from a JSON string
pipeline_run_instance = PipelineRun.from_json(json)
# print the JSON string representation of the object
print PipelineRun.to_json()

# convert the object into a dict
pipeline_run_dict = pipeline_run_instance.to_dict()
# create an instance of PipelineRun from a dict
pipeline_run_form_dict = pipeline_run.from_dict(pipeline_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


