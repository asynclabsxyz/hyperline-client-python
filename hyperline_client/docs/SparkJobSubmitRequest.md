# SparkJobSubmitRequest

A request object for submitting a Spark job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**python_file** | **str** |  | 
**job_name** | **str** |  | [optional] 
**args** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.spark_job_submit_request import SparkJobSubmitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJobSubmitRequest from a JSON string
spark_job_submit_request_instance = SparkJobSubmitRequest.from_json(json)
# print the JSON string representation of the object
print SparkJobSubmitRequest.to_json()

# convert the object into a dict
spark_job_submit_request_dict = spark_job_submit_request_instance.to_dict()
# create an instance of SparkJobSubmitRequest from a dict
spark_job_submit_request_form_dict = spark_job_submit_request.from_dict(spark_job_submit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


