# PipelineBackfillRequest

A pipeline backfill request object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** |  | 
**argument_name** | **str** |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | 
**interval** | **int** |  | [optional] 

## Example

```python
from hyperline_client.models.pipeline_backfill_request import PipelineBackfillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PipelineBackfillRequest from a JSON string
pipeline_backfill_request_instance = PipelineBackfillRequest.from_json(json)
# print the JSON string representation of the object
print PipelineBackfillRequest.to_json()

# convert the object into a dict
pipeline_backfill_request_dict = pipeline_backfill_request_instance.to_dict()
# create an instance of PipelineBackfillRequest from a dict
pipeline_backfill_request_form_dict = pipeline_backfill_request.from_dict(pipeline_backfill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


