# PipelineImportError

A pipeline import error.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The import error ID. | [optional] 
**timestamp** | **str** | The time when this error was created. | [optional] 
**file_name** | **str** | The file name of the associated DAG file. | [optional] 
**stack_trace** | **str** | The full stackstrace from Airflow. | [optional] 

## Example

```python
from hyperline_client.models.pipeline_import_error import PipelineImportError

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineImportError from a JSON string
pipeline_import_error_instance = PipelineImportError.from_json(json)
# print the JSON string representation of the object
print PipelineImportError.to_json()

# convert the object into a dict
pipeline_import_error_dict = pipeline_import_error_instance.to_dict()
# create an instance of PipelineImportError from a dict
pipeline_import_error_form_dict = pipeline_import_error.from_dict(pipeline_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


