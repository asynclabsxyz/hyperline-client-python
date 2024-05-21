# ItemizedCost

All in unit of cents.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigquery** | **int** |  | [optional] 
**gcs** | **int** |  | [optional] 
**trino** | **int** |  | [optional] 
**dataproc** | **int** |  | [optional] 
**snowflake** | **int** |  | [optional] 
**airflow** | **int** |  | [optional] 
**jupyter** | **int** |  | [optional] 
**gke** | **int** |  | [optional] 

## Example

```python
from hyperline_client.models.itemized_cost import ItemizedCost

# TODO update the JSON string below
json = "{}"
# create an instance of ItemizedCost from a JSON string
itemized_cost_instance = ItemizedCost.from_json(json)
# print the JSON string representation of the object
print ItemizedCost.to_json()

# convert the object into a dict
itemized_cost_dict = itemized_cost_instance.to_dict()
# create an instance of ItemizedCost from a dict
itemized_cost_form_dict = itemized_cost.from_dict(itemized_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


