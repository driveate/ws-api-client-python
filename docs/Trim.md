# Trim

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Combined trim, body, and generation identifier. Non-unique through markets (e.g. &#x60;20-gg2w-iii-restyling&#x60;) | 
**name** | **str** | Format: __*&#x60;trim (body) [generation]&#x60;*__ (e.g. &#x60;2.0 (GG2W) [III Restyling]&#x60;) | [optional] 
**trim** | **str** | Trim name. It can be empty for models created for JDM market (e.g. &#x60;2.0&#x60;, can be __*&#x60;null&#x60;*__) | 
**body** | **str** | Body name. Used extensively for JDM market (e.g. &#x60;GG2W&#x60;, can be __*&#x60;null&#x60;*__) | 
**generation** | **str** | Generation name (e.g. &#x60;III Restyling&#x60;, can be __*&#x60;null&#x60;*__) | [optional] 
**production_start_year** | **int** | Trim production start year (e.g. &#x60;2015&#x60;, can be __*&#x60;null&#x60;*__) | 
**production_end_year** | **int** | Trim production end year (e.g. &#x60;2016&#x60;, can be __*&#x60;null&#x60;*__) | 
**markets** | [**list[Market]**](Market.md) | List of markets where this trim if present | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


