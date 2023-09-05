# FileCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[File]**](File.md) |  | 

## Example

```python
from hyperline_client.models.file_collection import FileCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FileCollection from a JSON string
file_collection_instance = FileCollection.from_json(json)
# print the JSON string representation of the object
print FileCollection.to_json()

# convert the object into a dict
file_collection_dict = file_collection_instance.to_dict()
# create an instance of FileCollection from a dict
file_collection_form_dict = file_collection.from_dict(file_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


