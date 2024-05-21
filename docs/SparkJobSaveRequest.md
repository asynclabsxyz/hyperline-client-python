# SparkJobSaveRequest

A request object for saving a Spark job to pipeline.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | 
**schedule** | **str** |  | 

## Example

```python
from hyperline_client.models.spark_job_save_request import SparkJobSaveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJobSaveRequest from a JSON string
spark_job_save_request_instance = SparkJobSaveRequest.from_json(json)
# print the JSON string representation of the object
print SparkJobSaveRequest.to_json()

# convert the object into a dict
spark_job_save_request_dict = spark_job_save_request_instance.to_dict()
# create an instance of SparkJobSaveRequest from a dict
spark_job_save_request_form_dict = spark_job_save_request.from_dict(spark_job_save_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


