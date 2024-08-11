# OrgUsageDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**costs** | [**List[DatedItemizedCost]**](DatedItemizedCost.md) |  | [optional] 

## Example

```python
from hyperline_client.models.org_usage_details import OrgUsageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsageDetails from a JSON string
org_usage_details_instance = OrgUsageDetails.from_json(json)
# print the JSON string representation of the object
print OrgUsageDetails.to_json()

# convert the object into a dict
org_usage_details_dict = org_usage_details_instance.to_dict()
# create an instance of OrgUsageDetails from a dict
org_usage_details_form_dict = org_usage_details.from_dict(org_usage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


