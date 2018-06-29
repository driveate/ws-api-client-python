# Vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market** | [**Market**](Market.md) |  | [optional] 
**body** | **str** | Body name. Used extensively for JDM market (e.g. &#x60;GG2W&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**trim** | **str** | Trim name. It can be empty for models created for JDM market (e.g. &#x60;2.0&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**slug** | **str** | Combined trim, body, and generation identifier. Non-unique through markets (e.g. &#x60;20-gg2w-iii-restyling&#x60;) | [optional] 
**generation** | [**Generation**](Generation.md) |  | [optional] 
**stud_holes** | **int** | Number of stud holes (e.g. &#x60;5&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**pcd** | **float** | Pitch circle diameter, mm (e.g. &#x60;105&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**centre_bore** | **float** | Centre bore diameter, mm (e.g. &#x60;48.1&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**lock_type** | **str** |  | [optional] 
**lock_text** | **str** | Lock thread size (e.g. &#x60;M12 x 1.25&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**bolt_pattern** | **str** | Bolt pattern (e.g. &#x60;5x105&#x60;, can be __*&#x60;N/A&#x60;*__) | [optional] 
**power** | [**Power**](Power.md) |  | [optional] 
**engine_type** | **str** | Engine type (e.g. &#x60;V8&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**fuel** | **str** | Fuel (e.g. &#x60;Petrol&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**wheels** | [**list[WheelPair]**](WheelPair.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


