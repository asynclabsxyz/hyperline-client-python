# SqlJobStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**duration** | **int** |  | [optional] 
**total_bytes_processed** | **int** |  | [optional] 

## Example

```python
from hyperline_client.models.sql_job_statistics import SqlJobStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of SqlJobStatistics from a JSON string
sql_job_statistics_instance = SqlJobStatistics.from_json(json)
# print the JSON string representation of the object
print SqlJobStatistics.to_json()

# convert the object into a dict
sql_job_statistics_dict = sql_job_statistics_instance.to_dict()
# create an instance of SqlJobStatistics from a dict
sql_job_statistics_form_dict = sql_job_statistics.from_dict(sql_job_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


