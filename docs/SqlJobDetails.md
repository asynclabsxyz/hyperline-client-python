# SqlJobDetails

A SQL job status object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**engine** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**job_status** | **str** |  | 
**submitted_by** | **str** |  | [optional] 
**statistics** | [**SqlJobStatistics**](SqlJobStatistics.md) |  | [optional] 

## Example

```python
from hyperline_client.models.sql_job_details import SqlJobDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SqlJobDetails from a JSON string
sql_job_details_instance = SqlJobDetails.from_json(json)
# print the JSON string representation of the object
print SqlJobDetails.to_json()

# convert the object into a dict
sql_job_details_dict = sql_job_details_instance.to_dict()
# create an instance of SqlJobDetails from a dict
sql_job_details_form_dict = sql_job_details.from_dict(sql_job_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


