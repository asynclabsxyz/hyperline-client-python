# PipelineMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**author_email** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**last_updated_at** | **datetime** |  | [optional] 
**last_executed_at** | **datetime** |  | [optional] 

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


