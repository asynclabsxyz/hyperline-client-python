# SavedJobCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_jobs** | [**List[SavedJob]**](SavedJob.md) |  | [optional] 

## Example

```python
from hyperline_client.models.saved_job_collection import SavedJobCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SavedJobCollection from a JSON string
saved_job_collection_instance = SavedJobCollection.from_json(json)
# print the JSON string representation of the object
print SavedJobCollection.to_json()

# convert the object into a dict
saved_job_collection_dict = saved_job_collection_instance.to_dict()
# create an instance of SavedJobCollection from a dict
saved_job_collection_form_dict = saved_job_collection.from_dict(saved_job_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


