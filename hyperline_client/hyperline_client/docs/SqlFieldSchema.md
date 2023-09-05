# SqlFieldSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**precision** | **int** |  | [optional] 
**scale** | **int** |  | [optional] 

## Example

```python
from hyperline_client.models.sql_field_schema import SqlFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SqlFieldSchema from a JSON string
sql_field_schema_instance = SqlFieldSchema.from_json(json)
# print the JSON string representation of the object
print SqlFieldSchema.to_json()

# convert the object into a dict
sql_field_schema_dict = sql_field_schema_instance.to_dict()
# create an instance of SqlFieldSchema from a dict
sql_field_schema_form_dict = sql_field_schema.from_dict(sql_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


