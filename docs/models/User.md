# hyperline_client.model.user.User

A user object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A user object. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**role** | str,  | str,  | The user&#x27;s role | must be one of ["user", "admin", ] 
**organization** | str,  | str,  | The user&#x27;s organization name | 
**name** | str,  | str,  | The user&#x27;s name | 
**email** | str,  | str,  | The user&#x27;s email | [optional] 
**joined** | str, datetime,  | str,  | The datetime the user joined | [optional] value must conform to RFC-3339 date-time
**secrets** | str,  | str,  | The user&#x27;s secrets | [optional] 
**status** | str,  | str,  | The user&#x27;s status | [optional] must be one of ["active", "inactive", ] 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The user&#x27;s org id | [optional] value must be a 32 bit integer
**impersonated_user** | str,  | str,  | The user&#x27;s impersonated user | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

