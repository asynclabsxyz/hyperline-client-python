# SqlTable

A SQL table object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**columns** | [**List[SqlColumn]**](SqlColumn.md) |  | [optional] 

## Example

```python
from hyperline_client.models.sql_table import SqlTable

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTable from a JSON string
sql_table_instance = SqlTable.from_json(json)
# print the JSON string representation of the object
print SqlTable.to_json()

# convert the object into a dict
sql_table_dict = sql_table_instance.to_dict()
# create an instance of SqlTable from a dict
sql_table_form_dict = sql_table.from_dict(sql_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


