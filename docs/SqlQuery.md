# SqlQuery

A Sql Query object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_execution_token** | **str** | Continue execution of a query. When present, other fields are ignored. | [optional] 
**name** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 
**statement** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from hyperline_client.models.sql_query import SqlQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQuery from a JSON string
sql_query_instance = SqlQuery.from_json(json)
# print the JSON string representation of the object
print SqlQuery.to_json()

# convert the object into a dict
sql_query_dict = sql_query_instance.to_dict()
# create an instance of SqlQuery from a dict
sql_query_form_dict = sql_query.from_dict(sql_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


