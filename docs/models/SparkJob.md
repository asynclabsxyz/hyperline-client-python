# hyperline_client.model.spark_job.SparkJob

A Spark Job object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Spark Job object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The job id. | 
**name** | str,  | str,  | The job name. | [optional] 
**file** | str,  | str,  | The file path of the Spark program. | [optional] 
**type** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**submitted_by** | str,  | str,  | The email of the submitter. | [optional] 
**submitted_on** | str,  | str,  |  | [optional] 
**duration** | decimal.Decimal, int,  | decimal.Decimal,  | The duration of the job in seconds. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

