# SqlExecuteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**var_schema** | [**List[SqlFieldSchema]**](SqlFieldSchema.md) |  | [optional] 
**rows** | **List[object]** |  | [optional] 
**statistics** | [**SqlJobStatistics**](SqlJobStatistics.md) |  | [optional] 

## Example

```python
from hyperline_client.models.sql_execute_response import SqlExecuteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SqlExecuteResponse from a JSON string
sql_execute_response_instance = SqlExecuteResponse.from_json(json)
# print the JSON string representation of the object
print SqlExecuteResponse.to_json()

# convert the object into a dict
sql_execute_response_dict = sql_execute_response_instance.to_dict()
# create an instance of SqlExecuteResponse from a dict
sql_execute_response_form_dict = sql_execute_response.from_dict(sql_execute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


