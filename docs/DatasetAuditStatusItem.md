# DatasetAuditStatusItem

Metric for audit status item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_status_item import DatasetAuditStatusItem

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditStatusItem from a JSON string
dataset_audit_status_item_instance = DatasetAuditStatusItem.from_json(json)
# print the JSON string representation of the object
print DatasetAuditStatusItem.to_json()

# convert the object into a dict
dataset_audit_status_item_dict = dataset_audit_status_item_instance.to_dict()
# create an instance of DatasetAuditStatusItem from a dict
dataset_audit_status_item_form_dict = dataset_audit_status_item.from_dict(dataset_audit_status_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


