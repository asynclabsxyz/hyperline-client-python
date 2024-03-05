# OrgUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_end_date** | **date** | The date when the trial period ends. | [optional] 
**trial_limit_in_cents** | **int** | Dollar limit for trial period in cents. | [optional] 
**total_usage_in_cents** | **int** | Dollar amount used in cents. | [optional] 
**bytes_scanned** | **int** | Bytes scanned when querying data. | [optional] 
**compute_units_per_ms** | **int** | Data Compute Unit (DCU) used per millisecond. | [optional] 
**bytes_stored** | **int** | Bytes stored. | [optional] 

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


