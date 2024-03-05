# DatasetAuditStatus

Audit status of a dataset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** |  | [optional] 
**metrics** | [**List[DatasetAuditStatusItem]**](DatasetAuditStatusItem.md) |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_status import DatasetAuditStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditStatus from a JSON string
dataset_audit_status_instance = DatasetAuditStatus.from_json(json)
# print the JSON string representation of the object
print DatasetAuditStatus.to_json()

# convert the object into a dict
dataset_audit_status_dict = dataset_audit_status_instance.to_dict()
# create an instance of DatasetAuditStatus from a dict
dataset_audit_status_form_dict = dataset_audit_status.from_dict(dataset_audit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


