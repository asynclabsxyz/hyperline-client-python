# PipelineRunCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_runs** | [**List[PipelineRun]**](PipelineRun.md) |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_run_collection import PipelineRunCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineRunCollection from a JSON string
pipeline_run_collection_instance = PipelineRunCollection.from_json(json)
# print the JSON string representation of the object
print PipelineRunCollection.to_json()

# convert the object into a dict
pipeline_run_collection_dict = pipeline_run_collection_instance.to_dict()
# create an instance of PipelineRunCollection from a dict
pipeline_run_collection_form_dict = pipeline_run_collection.from_dict(pipeline_run_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


