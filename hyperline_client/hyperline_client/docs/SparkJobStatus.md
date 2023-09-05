# SparkJobStatus

A Spark job status object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**job_type** | **str** |  | [optional] 
**job_status** | **str** |  | 
**status_timestamp** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.spark_job_status import SparkJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJobStatus from a JSON string
spark_job_status_instance = SparkJobStatus.from_json(json)
# print the JSON string representation of the object
print SparkJobStatus.to_json()

# convert the object into a dict
spark_job_status_dict = spark_job_status_instance.to_dict()
# create an instance of SparkJobStatus from a dict
spark_job_status_form_dict = spark_job_status.from_dict(spark_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


