# SamplesCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**samples** | [**List[Sample]**](Sample.md) |  | 

## Example

```python
from hyperline_client.models.samples_collection import SamplesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SamplesCollection from a JSON string
samples_collection_instance = SamplesCollection.from_json(json)
# print the JSON string representation of the object
print SamplesCollection.to_json()

# convert the object into a dict
samples_collection_dict = samples_collection_instance.to_dict()
# create an instance of SamplesCollection from a dict
samples_collection_form_dict = samples_collection.from_dict(samples_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


