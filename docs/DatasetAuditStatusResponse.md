# DatasetAuditStatusResponse

Response object for data audit status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chains** | [**List[DatasetAuditStatus]**](DatasetAuditStatus.md) |  | [optional] 
**issues** | **List[str]** |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_status_response import DatasetAuditStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditStatusResponse from a JSON string
dataset_audit_status_response_instance = DatasetAuditStatusResponse.from_json(json)
# print the JSON string representation of the object
print DatasetAuditStatusResponse.to_json()

# convert the object into a dict
dataset_audit_status_response_dict = dataset_audit_status_response_instance.to_dict()
# create an instance of DatasetAuditStatusResponse from a dict
dataset_audit_status_response_form_dict = dataset_audit_status_response.from_dict(dataset_audit_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


