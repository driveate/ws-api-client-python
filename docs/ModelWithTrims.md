# ModelWithTrims

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | Model name (e.g. &#x60;Outlander&#x60;) | 
**name** | **str** | Model slug name (e.g. &#x60;outlander&#x60;) | 
**start_year** | **str** | Model production start year. It should be &#39;integer&#39; but it is used as &#39;string&#39; by historical reasons. | 
**end_year** | **str** | Model production end year. It should be &#39;integer&#39; but it is used as &#39;string&#39; by  historical reasons.  It equals to the __*&#x60;current year + 1&#x60;*__ if it is still in production. | 
**vehicles** | [**list[TrimWithMarketAndYears]**](TrimWithMarketAndYears.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


