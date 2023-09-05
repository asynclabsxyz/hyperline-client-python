# ExplorerViewDatasetCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[ExplorerViewDataset]**](ExplorerViewDataset.md) |  | [optional] 

## Example

```python
from hyperline_client.models.explorer_view_dataset_collection import ExplorerViewDatasetCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerViewDatasetCollection from a JSON string
explorer_view_dataset_collection_instance = ExplorerViewDatasetCollection.from_json(json)
# print the JSON string representation of the object
print ExplorerViewDatasetCollection.to_json()

# convert the object into a dict
explorer_view_dataset_collection_dict = explorer_view_dataset_collection_instance.to_dict()
# create an instance of ExplorerViewDatasetCollection from a dict
explorer_view_dataset_collection_form_dict = explorer_view_dataset_collection.from_dict(explorer_view_dataset_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


