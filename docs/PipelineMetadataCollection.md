# PipelineMetadataCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_list** | [**List[PipelineMetadata]**](PipelineMetadata.md) |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_metadata_collection import PipelineMetadataCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineMetadataCollection from a JSON string
pipeline_metadata_collection_instance = PipelineMetadataCollection.from_json(json)
# print the JSON string representation of the object
print PipelineMetadataCollection.to_json()

# convert the object into a dict
pipeline_metadata_collection_dict = pipeline_metadata_collection_instance.to_dict()
# create an instance of PipelineMetadataCollection from a dict
pipeline_metadata_collection_form_dict = pipeline_metadata_collection.from_dict(pipeline_metadata_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


