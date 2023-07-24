# hyperline_client.model.pipeline_backfill_request.PipelineBackfillRequest

A pipeline backfill request object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A pipeline backfill request object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**argument_name** | str,  | str,  |  | 
**end_date** | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD
**pipeline_name** | str,  | str,  |  | 
**start_date** | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD
**interval** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

