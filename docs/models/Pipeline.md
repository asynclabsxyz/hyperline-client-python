# hyperline_client.model.pipeline.Pipeline

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[stages](#stages)** | list, tuple,  | tuple,  | The list of the stages of the pipeline. | 
**pipeline_name** | str,  | str,  | The name of the pipeline. | 
**schedule** | str,  | str,  | The schedule of the pipeline. | [optional] 
**max_active_runs** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of active runs for a DAG. | [optional] 
**retries** | decimal.Decimal, int,  | decimal.Decimal,  | The number of retries that should be performed before failing a task. | [optional] 
**start_date** |  |  | The date at which the pipeline&#x27;s schedule starts. | [optional] 
**catchup** | bool,  | BoolClass,  | Kickoff DAG runs for data intervals that have not been run since the last data interval. | [optional] 
**write_test_mode** | bool,  | BoolClass,  | Write output data in a test database. | [optional] 
**sample_reads** | bool,  | BoolClass,  | Read a sample of input data from datasource. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# stages

The list of the stages of the pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of the stages of the pipeline. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Stage**](Stage.md) | [**Stage**](Stage.md) | [**Stage**](Stage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

