# PipelineMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**owners** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**schedule** | **str** |  | [optional] 
**last_run** | **datetime** |  | [optional] 
**next_run** | **datetime** |  | [optional] 
**has_import_errors** | **bool** |  | [optional] 
**file_location** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_metadata import PipelineMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineMetadata from a JSON string
pipeline_metadata_instance = PipelineMetadata.from_json(json)
# print the JSON string representation of the object
print PipelineMetadata.to_json()

# convert the object into a dict
pipeline_metadata_dict = pipeline_metadata_instance.to_dict()
# create an instance of PipelineMetadata from a dict
pipeline_metadata_form_dict = pipeline_metadata.from_dict(pipeline_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


