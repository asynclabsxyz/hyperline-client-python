# SqlColumn

A SQL column object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**nullable** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.sql_column import SqlColumn

# TODO update the JSON string below
json = "{}"
# create an instance of SqlColumn from a JSON string
sql_column_instance = SqlColumn.from_json(json)
# print the JSON string representation of the object
print SqlColumn.to_json()

# convert the object into a dict
sql_column_dict = sql_column_instance.to_dict()
# create an instance of SqlColumn from a dict
sql_column_form_dict = sql_column.from_dict(sql_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


