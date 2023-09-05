# SqlJobStatus

A SQL job status object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**job_type** | **str** |  | [optional] 
**job_status** | **str** |  | 

## Example

```python
from hyperline_client.models.sql_job_status import SqlJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SqlJobStatus from a JSON string
sql_job_status_instance = SqlJobStatus.from_json(json)
# print the JSON string representation of the object
print SqlJobStatus.to_json()

# convert the object into a dict
sql_job_status_dict = sql_job_status_instance.to_dict()
# create an instance of SqlJobStatus from a dict
sql_job_status_form_dict = sql_job_status.from_dict(sql_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


