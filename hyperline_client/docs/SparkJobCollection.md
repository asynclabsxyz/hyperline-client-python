# SparkJobCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spark_jobs** | [**List[SparkJob]**](SparkJob.md) |  | [optional] 

## Example

```python
from hyperline_client.models.spark_job_collection import SparkJobCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SparkJobCollection from a JSON string
spark_job_collection_instance = SparkJobCollection.from_json(json)
# print the JSON string representation of the object
print SparkJobCollection.to_json()

# convert the object into a dict
spark_job_collection_dict = spark_job_collection_instance.to_dict()
# create an instance of SparkJobCollection from a dict
spark_job_collection_form_dict = spark_job_collection.from_dict(spark_job_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


