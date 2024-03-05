# DatasetAuditDetailsItem

Audit details for a chain.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **str** |  | [optional] 
**details** | **List[str]** |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_details_item import DatasetAuditDetailsItem

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditDetailsItem from a JSON string
dataset_audit_details_item_instance = DatasetAuditDetailsItem.from_json(json)
# print the JSON string representation of the object
print DatasetAuditDetailsItem.to_json()

# convert the object into a dict
dataset_audit_details_item_dict = dataset_audit_details_item_instance.to_dict()
# create an instance of DatasetAuditDetailsItem from a dict
dataset_audit_details_item_form_dict = dataset_audit_details_item.from_dict(dataset_audit_details_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


