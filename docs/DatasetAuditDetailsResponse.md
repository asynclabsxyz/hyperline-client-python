# DatasetAuditDetailsResponse

Response object for dataset audit details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | [**List[DatasetAuditDetails]**](DatasetAuditDetails.md) |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_details_response import DatasetAuditDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditDetailsResponse from a JSON string
dataset_audit_details_response_instance = DatasetAuditDetailsResponse.from_json(json)
# print the JSON string representation of the object
print DatasetAuditDetailsResponse.to_json()

# convert the object into a dict
dataset_audit_details_response_dict = dataset_audit_details_response_instance.to_dict()
# create an instance of DatasetAuditDetailsResponse from a dict
dataset_audit_details_response_form_dict = dataset_audit_details_response.from_dict(dataset_audit_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


