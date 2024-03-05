# ExplorerViewDataset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**children** | [**List[ExplorerViewDataset]**](ExplorerViewDataset.md) |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**in_preview** | **bool** |  | [optional] 

## Example

```python
from hyperline_client.models.explorer_view_dataset import ExplorerViewDataset

# TODO update the JSON string below
json = "{}"
# create an instance of ExplorerViewDataset from a JSON string
explorer_view_dataset_instance = ExplorerViewDataset.from_json(json)
# print the JSON string representation of the object
print ExplorerViewDataset.to_json()

# convert the object into a dict
explorer_view_dataset_dict = explorer_view_dataset_instance.to_dict()
# create an instance of ExplorerViewDataset from a dict
explorer_view_dataset_form_dict = explorer_view_dataset.from_dict(explorer_view_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


