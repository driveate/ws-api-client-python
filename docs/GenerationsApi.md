# ws_api_client.GenerationsApi

All URIs are relative to *https://api.wheel-size.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generations_list**](GenerationsApi.md#generations_list) | **GET** /generations/ | Generations for the given model


# **generations_list**
> list[GenerationWithMakeAndModel] generations_list(make, model, year=year, lang=lang)

Generations for the given model

Get a list of generations for the given model. It is possible to retrieve generations for specific year.

### Example
```python
from __future__ import print_function
import time
import ws_api_client
from ws_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user_key
configuration = ws_api_client.Configuration()
configuration.api_key['user_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user_key'] = 'Bearer'

# create an instance of the API class
api_instance = ws_api_client.GenerationsApi(ws_api_client.ApiClient(configuration))
make = '\"mitsubishi\"' # str | Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`)
model = '\"outlander\"' # str | Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`)
year = 56 # int | You can use _**`GET /years/`**_ to get possible years (e.g. `2015`) (optional)
lang = 'lang_example' # str | Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn,zh-tw`. Currently translation works for chinese `zh-cn` language only (optional)

try:
    # Generations for the given model
    api_response = api_instance.generations_list(make, model, year=year, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenerationsApi->generations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make** | **str**| Manufacturer slug name, use _**&#x60;GET /makes/&#x60;**_ to get possible values (e.g. &#x60;mitsubishi&#x60;) | 
 **model** | **str**| Model slug name, use _**&#x60;GET /models/&#x60;**_ to get possible values (e.g. &#x60;outlander&#x60;) | 
 **year** | **int**| You can use _**&#x60;GET /years/&#x60;**_ to get possible years (e.g. &#x60;2015&#x60;) | [optional] 
 **lang** | **str**| Use this parameter anywhere in the API to get *&#x60;name&#x60;* field translation of the following objects: **&#x60;Make&#x60;**, **&#x60;Model&#x60;**, **&#x60;Market&#x60;**. Across the *&#x60;name&#x60;* this objects will have *&#x60;name_en&#x60;* field with original english name. By default &#x60;en&#x60; language is used.  Available languages: &#x60;en,de,ru,es,pt,fr,ja,zh-cn,zh-tw&#x60;. Currently translation works for chinese &#x60;zh-cn&#x60; language only | [optional] 

### Return type

[**list[GenerationWithMakeAndModel]**](GenerationWithMakeAndModel.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

