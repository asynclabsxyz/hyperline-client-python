# JobCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[Job]**](Job.md) |  | [optional] 
**stats** | [**List[JobsStat]**](JobsStat.md) |  | [optional] 

## Example

```python
from hyperline_client.models.job_collection import JobCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobCollection from a JSON string
job_collection_instance = JobCollection.from_json(json)
# print the JSON string representation of the object
print JobCollection.to_json()

# convert the object into a dict
job_collection_dict = job_collection_instance.to_dict()
# create an instance of JobCollection from a dict
job_collection_form_dict = job_collection.from_dict(job_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


