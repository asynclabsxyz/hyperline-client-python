# SqlQueryCollection

A Sql Query collection object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[SqlQuery]**](SqlQuery.md) |  | [optional] 

## Example

```python
from hyperline_client.models.sql_query_collection import SqlQueryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryCollection from a JSON string
sql_query_collection_instance = SqlQueryCollection.from_json(json)
# print the JSON string representation of the object
print SqlQueryCollection.to_json()

# convert the object into a dict
sql_query_collection_dict = sql_query_collection_instance.to_dict()
# create an instance of SqlQueryCollection from a dict
sql_query_collection_form_dict = sql_query_collection.from_dict(sql_query_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


