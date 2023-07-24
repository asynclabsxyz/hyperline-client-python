# hyperline_client.model.dataset.Dataset

A dataset object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A dataset object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**chain** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**big_query_reference** | str,  | str,  |  | [optional] 
**spark_reference** | str,  | str,  |  | [optional] 
**SQLDBReference** | str,  | str,  |  | [optional] 
**[tables](#tables)** | list, tuple,  | tuple,  |  | [optional] 
**[children](#children)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tables

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DatasetTable**](DatasetTable.md) | [**DatasetTable**](DatasetTable.md) | [**DatasetTable**](DatasetTable.md) |  | 

# children

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Dataset**](Dataset.md) | [**Dataset**](Dataset.md) | [**Dataset**](Dataset.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

