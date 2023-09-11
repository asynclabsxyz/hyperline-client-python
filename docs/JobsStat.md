# JobsStat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.jobs_stat import JobsStat

# TODO update the JSON string below
json = "{}"
# create an instance of JobsStat from a JSON string
jobs_stat_instance = JobsStat.from_json(json)
# print the JSON string representation of the object
print JobsStat.to_json()

# convert the object into a dict
jobs_stat_dict = jobs_stat_instance.to_dict()
# create an instance of JobsStat from a dict
jobs_stat_form_dict = jobs_stat.from_dict(jobs_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


