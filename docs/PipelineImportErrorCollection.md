# PipelineImportErrorCollection

A collection of pipeline import errors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_import_errors** | [**List[PipelineImportError]**](PipelineImportError.md) |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_import_error_collection import PipelineImportErrorCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineImportErrorCollection from a JSON string
pipeline_import_error_collection_instance = PipelineImportErrorCollection.from_json(json)
# print the JSON string representation of the object
print PipelineImportErrorCollection.to_json()

# convert the object into a dict
pipeline_import_error_collection_dict = pipeline_import_error_collection_instance.to_dict()
# create an instance of PipelineImportErrorCollection from a dict
pipeline_import_error_collection_form_dict = pipeline_import_error_collection.from_dict(pipeline_import_error_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


