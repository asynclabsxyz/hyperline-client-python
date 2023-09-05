# DatasetCollection

A dataset collection object containing raw and/or processed datasets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_datasets** | [**List[Dataset]**](Dataset.md) |  | [optional] 
**processed_datesets** | [**List[Dataset]**](Dataset.md) |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_collection import DatasetCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetCollection from a JSON string
dataset_collection_instance = DatasetCollection.from_json(json)
# print the JSON string representation of the object
print DatasetCollection.to_json()

# convert the object into a dict
dataset_collection_dict = dataset_collection_instance.to_dict()
# create an instance of DatasetCollection from a dict
dataset_collection_form_dict = dataset_collection.from_dict(dataset_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


