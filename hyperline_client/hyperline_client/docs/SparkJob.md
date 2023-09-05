# SparkJob

A Spark Job object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The job id. | 
**name** | **str** | The job name. | [optional] 
**file** | **str** | The file path of the Spark program. | [optional] 
**type** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**submitted_by** | **str** | The email of the submitter. | [optional] 
**submitted_on** | **str** |  | [optional] 
**duration** | **int** | The duration of the job in seconds. | [optional] 

## Example

```python
from hyperline_client.models.spark_job import SparkJob

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJob from a JSON string
spark_job_instance = SparkJob.from_json(json)
# print the JSON string representation of the object
print SparkJob.to_json()

# convert the object into a dict
spark_job_dict = spark_job_instance.to_dict()
# create an instance of SparkJob from a dict
spark_job_form_dict = spark_job.from_dict(spark_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


