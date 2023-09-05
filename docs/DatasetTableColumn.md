# DatasetTableColumn

A dataset table column object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**is_nullable** | **bool** |  | [optional] 
**is_partition_key** | **bool** |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_table_column import DatasetTableColumn

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetTableColumn from a JSON string
dataset_table_column_instance = DatasetTableColumn.from_json(json)
# print the JSON string representation of the object
print DatasetTableColumn.to_json()

# convert the object into a dict
dataset_table_column_dict = dataset_table_column_instance.to_dict()
# create an instance of DatasetTableColumn from a dict
dataset_table_column_form_dict = dataset_table_column.from_dict(dataset_table_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


