# FileCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**path** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**base64_contents** | **str** |  | [optional] 
**is_pipeline_dag_file** | **bool** |  | [optional] [default to False]

## Example

```python
from hyperline_client.models.file_create_request import FileCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileCreateRequest from a JSON string
file_create_request_instance = FileCreateRequest.from_json(json)
# print the JSON string representation of the object
print FileCreateRequest.to_json()

# convert the object into a dict
file_create_request_dict = file_create_request_instance.to_dict()
# create an instance of FileCreateRequest from a dict
file_create_request_form_dict = file_create_request.from_dict(file_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


