# DatasetAuditDetails

Audit details of a dataset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**chains** | [**List[DatasetAuditDetailsItem]**](DatasetAuditDetailsItem.md) |  | [optional] 

## Example

```python
from hyperline_client.models.dataset_audit_details import DatasetAuditDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAuditDetails from a JSON string
dataset_audit_details_instance = DatasetAuditDetails.from_json(json)
# print the JSON string representation of the object
print DatasetAuditDetails.to_json()

# convert the object into a dict
dataset_audit_details_dict = dataset_audit_details_instance.to_dict()
# create an instance of DatasetAuditDetails from a dict
dataset_audit_details_form_dict = dataset_audit_details.from_dict(dataset_audit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


