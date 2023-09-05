# DatasetTable

A dataset table object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_view** | **bool** |  | [optional] 
**columns** | [**List[DatasetTableColumn]**](DatasetTableColumn.md) |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_table import DatasetTable

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetTable from a JSON string
dataset_table_instance = DatasetTable.from_json(json)
# print the JSON string representation of the object
print DatasetTable.to_json()

# convert the object into a dict
dataset_table_dict = dataset_table_instance.to_dict()
# create an instance of DatasetTable from a dict
dataset_table_form_dict = dataset_table.from_dict(dataset_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


