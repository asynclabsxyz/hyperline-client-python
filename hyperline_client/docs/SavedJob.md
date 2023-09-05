# SavedJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The job name. | 
**type** | **str** | the job type. | 
**file** | **str** | The file path of the source code. | 
**package** | **str** | The package path if applicable. | [optional] 

## Example

```python
from hyperline_client.models.saved_job import SavedJob

# TODO update the JSON string below
json = "{}"
# create an instance of SavedJob from a JSON string
saved_job_instance = SavedJob.from_json(json)
# print the JSON string representation of the object
print SavedJob.to_json()

# convert the object into a dict
saved_job_dict = saved_job_instance.to_dict()
# create an instance of SavedJob from a dict
saved_job_form_dict = saved_job.from_dict(saved_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


