# DeleteOpResponse

Response object for delete operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] [readonly] 
**message** | **str** |  | [optional] [readonly] 

## Example

```python
from hyperline_client.models.delete_op_response import DeleteOpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOpResponse from a JSON string
delete_op_response_instance = DeleteOpResponse.from_json(json)
# print the JSON string representation of the object
print DeleteOpResponse.to_json()

# convert the object into a dict
delete_op_response_dict = delete_op_response_instance.to_dict()
# create an instance of DeleteOpResponse from a dict
delete_op_response_form_dict = delete_op_response.from_dict(delete_op_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


