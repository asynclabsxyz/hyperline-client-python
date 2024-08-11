# UserOnboardingSteps

User's onboarding steps

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql_step** | **bool** |  | [optional] 
**spark_step** | **bool** |  | [optional] 
**notebook_step** | **bool** |  | [optional] 
**updated_at** | **datetime** | The datetime the onboarding steps were last updated | [optional] 

## Example

```python
from hyperline_client.models.user_onboarding_steps import UserOnboardingSteps

# TODO update the JSON string below
json = "{}"
# create an instance of UserOnboardingSteps from a JSON string
user_onboarding_steps_instance = UserOnboardingSteps.from_json(json)
# print the JSON string representation of the object
print UserOnboardingSteps.to_json()

# convert the object into a dict
user_onboarding_steps_dict = user_onboarding_steps_instance.to_dict()
# create an instance of UserOnboardingSteps from a dict
user_onboarding_steps_form_dict = user_onboarding_steps.from_dict(user_onboarding_steps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


