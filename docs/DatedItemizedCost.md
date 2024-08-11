# DatedItemizedCost

All in unit of cents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | [**ItemizedCost**](ItemizedCost.md) |  | [optional] 
**var_date** | **date** | The date of the itemized cost. | [optional] 

## Example

```python
from hyperline_client.models.dated_itemized_cost import DatedItemizedCost

# TODO update the JSON string below
json = "{}"
# create an instance of DatedItemizedCost from a JSON string
dated_itemized_cost_instance = DatedItemizedCost.from_json(json)
# print the JSON string representation of the object
print DatedItemizedCost.to_json()

# convert the object into a dict
dated_itemized_cost_dict = dated_itemized_cost_instance.to_dict()
# create an instance of DatedItemizedCost from a dict
dated_itemized_cost_form_dict = dated_itemized_cost.from_dict(dated_itemized_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


