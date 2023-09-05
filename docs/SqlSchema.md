# SqlSchema

A SQL schema object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[SqlTable]**](SqlTable.md) |  | [optional] 

## Example

```python
from hyperline_client.models.sql_schema import SqlSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SqlSchema from a JSON string
sql_schema_instance = SqlSchema.from_json(json)
# print the JSON string representation of the object
print SqlSchema.to_json()

# convert the object into a dict
sql_schema_dict = sql_schema_instance.to_dict()
# create an instance of SqlSchema from a dict
sql_schema_form_dict = sql_schema.from_dict(sql_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


