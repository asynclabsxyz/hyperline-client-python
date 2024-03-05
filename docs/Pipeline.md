# Pipeline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_name** | **str** | The name of the pipeline, equivalent to DAG_ID in Airflow.  Must consist exclusively of alphanumeric characters, dashes, dots and underscores (all ASCII).  | [optional] 
**raw_code** | **str** | The raw python code for the DAG. | [optional] 
**schedule** | **str** | The schedule of the pipeline. | [optional] 
**stages** | [**List[Stage]**](Stage.md) | The list of the stages of the pipeline. | [optional] 
**max_active_runs** | **int** | The maximum number of active runs for a DAG. | [optional] 
**retries** | **int** | The number of retries that should be performed before failing a task. | [optional] 
**start_date** | **date** | The date at which the pipeline&#39;s schedule starts. | [optional] 
**catchup** | **bool** | Kickoff DAG runs for data intervals that have not been run since the last data interval. | [optional] 
**write_test_mode** | **bool** | Write output data in a test database. | [optional] 
**sample_reads** | **bool** | Read a sample of input data from datasource. | [optional] 

## Example

```python
from hyperline_client.models.pipeline import Pipeline

# TODO update the JSON string below
json = "{}"
# create an instance of Pipeline from a JSON string
pipeline_instance = Pipeline.from_json(json)
# print the JSON string representation of the object
print Pipeline.to_json()

# convert the object into a dict
pipeline_dict = pipeline_instance.to_dict()
# create an instance of Pipeline from a dict
pipeline_form_dict = pipeline.from_dict(pipeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


