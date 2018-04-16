# Vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market** | [**Market**](Market.md) |  | 
**body** | **str** | Body name. Used extensively for JDM market (e.g. &#x60;GG2W&#x60;, can be __*&#x60;null&#x60;*__) | 
**trim** | **str** | Trim name. It can be empty for models created for JDM market (e.g. &#x60;2.0&#x60;, can be __*&#x60;null&#x60;*__) | 
**generation** | [**Generation**](Generation.md) |  | 
**stud_holes** | **int** | Number of stud holes (e.g. &#x60;5&#x60;, can be __*&#x60;null&#x60;*__) | 
**pcd** | **float** | Pitch circle diameter, mm (e.g. &#x60;105&#x60;, can be __*&#x60;null&#x60;*__) | 
**centre_bore** | **float** | Centre bore diameter, mm (e.g. &#x60;48.1&#x60;, can be __*&#x60;null&#x60;*__) | 
**lock_type** | **str** |  | [optional] 
**lock_text** | **str** | Lock thread size (e.g. &#x60;M12 x 1.25&#x60;, can be __*&#x60;null&#x60;*__) | 
**bolt_pattern** | **str** | Bolt pattern (e.g. &#x60;5x105&#x60;, can be __*&#x60;N/A&#x60;*__) | 
**power** | [**Power**](Power.md) |  | [optional] 
**fuel** | **str** | Fuel (e.g. &#x60;Petrol&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**wheels** | [**list[WheelPair]**](WheelPair.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


