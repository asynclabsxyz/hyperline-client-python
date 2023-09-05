# SparkJobOutput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**job_type** | **str** |  | [optional] 
**job_status** | **str** |  | 
**status_timestamp** | **str** |  | [optional] 
**job_output** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.spark_job_output import SparkJobOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJobOutput from a JSON string
spark_job_output_instance = SparkJobOutput.from_json(json)
# print the JSON string representation of the object
print SparkJobOutput.to_json()

# convert the object into a dict
spark_job_output_dict = spark_job_output_instance.to_dict()
# create an instance of SparkJobOutput from a dict
spark_job_output_form_dict = spark_job_output.from_dict(spark_job_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


