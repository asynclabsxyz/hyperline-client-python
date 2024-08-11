# OrgUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** | ID of the org. | [optional] 
**trial_end_date** | **date** | The date when the trial period ends. | [optional] 
**trial_limit_in_cents** | **int** | Dollar limit for trial period in cents. | [optional] 
**total_usage_in_cents** | **int** | Dollar amount used in cents. | [optional] 
**itemized_cost** | [**ItemizedCost**](ItemizedCost.md) |  | [optional] 

## Example

```python
from hyperline_client.models.org_usage import OrgUsage

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUsage from a JSON string
org_usage_instance = OrgUsage.from_json(json)
# print the JSON string representation of the object
print OrgUsage.to_json()

# convert the object into a dict
org_usage_dict = org_usage_instance.to_dict()
# create an instance of OrgUsage from a dict
org_usage_form_dict = org_usage.from_dict(org_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


