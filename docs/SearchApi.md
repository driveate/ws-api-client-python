# ws_api_client.SearchApi

All URIs are relative to *https://api.wheel-size.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_by_hf_tire_list**](SearchApi.md#search_by_hf_tire_list) | **GET** /search/by_hf_tire/ | Find models matching given high flotation tire
[**search_by_model_list**](SearchApi.md#search_by_model_list) | **GET** /search/by_model/ | Find OE and option fitments by model/year/trim
[**search_by_rim_list**](SearchApi.md#search_by_rim_list) | **GET** /search/by_rim/ | Find models matching given rim parameters
[**search_by_tire_list**](SearchApi.md#search_by_tire_list) | **GET** /search/by_tire/ | Find models matching given tire parameters


# **search_by_hf_tire_list**
> list[MakeWithModels] search_by_hf_tire_list(tire_diameter, tire_section_width, rim_diameter_hf, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)

Find models matching given high flotation tire

Get a list of model modifications that match the given tire size in high flotation sizing system

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
api_instance = ws_api_client.SearchApi(ws_api_client.ApiClient(configuration))
tire_diameter = 31 # float | Tire diameter, in (e.g. `31`)
tire_section_width = 10.5 # float | Tire section width, in (e.g. `10.5`)
rim_diameter_hf = 15 # float | Rim diameter, in (e.g. `15`)
lang = 'lang_example' # str | Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only (optional)
brands = 'brands_example' # str | Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`) (optional)
brands_exclude = 'brands_exclude_example' # str | Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`) (optional)
countries = 'countries_example' # str | Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`) (optional)
countries_exclude = 'countries_exclude_example' # str | Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`) (optional)

try:
    # Find models matching given high flotation tire
    api_response = api_instance.search_by_hf_tire_list(tire_diameter, tire_section_width, rim_diameter_hf, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_by_hf_tire_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tire_diameter** | **float**| Tire diameter, in (e.g. &#x60;31&#x60;) | 
 **tire_section_width** | **float**| Tire section width, in (e.g. &#x60;10.5&#x60;) | 
 **rim_diameter_hf** | **float**| Rim diameter, in (e.g. &#x60;15&#x60;) | 
 **lang** | **str**| Use this parameter anywhere in the API to get *&#x60;name&#x60;* field translation of the following objects: **&#x60;Make&#x60;**, **&#x60;Model&#x60;**, **&#x60;Market&#x60;**. Across the *&#x60;name&#x60;* this objects will have *&#x60;name_en&#x60;* field with original english name. By default &#x60;en&#x60; language is used.  Available languages: &#x60;en,de,ru,es,pt,fr,ja,zh-cn&#x60;. Currently translation works for chinese &#x60;zh-cn&#x60; language only | [optional] 
 **brands** | **str**| Show information only for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;mitsubishi,nissan,toyota&#x60;) | [optional] 
 **brands_exclude** | **str**| Don&#39;t show information for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;geely,great-wall&#x60;) | [optional] 
 **countries** | **str**| Show information for local manufacturers from specified countries only. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;us,gb,jp&#x60;) | [optional] 
 **countries_exclude** | **str**| Don&#39;t show information for local manufacturers from specified countries. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;ru,ua&#x60;) | [optional] 

### Return type

[**list[MakeWithModels]**](MakeWithModels.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_model_list**
> list[Vehicle] search_by_model_list(make, model, year, trim=trim, only_oem=only_oem, lang=lang)

Find OE and option fitments by model/year/trim

Find OE and option fitments that match the given manufacturer, model, year and trim.  **It's an alias** for _**`GET /vehicles/`**_ method

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
api_instance = ws_api_client.SearchApi(ws_api_client.ApiClient(configuration))
make = '\"mitsubishi\"' # str | Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`)
model = '\"outlander\"' # str | Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`)
year = 2015 # int | You can use _**`GET /years/`**_ to get possible years (e.g. `2015`)
trim = 'trim_example' # str | Use *`slug`* from _**`GET /trims/`**_ methods here. (e.g. `2.0+GG2W`) (optional)
only_oem = true # bool | Show only original equipment wheels (optional)
lang = 'lang_example' # str | Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only (optional)

try:
    # Find OE and option fitments by model/year/trim
    api_response = api_instance.search_by_model_list(make, model, year, trim=trim, only_oem=only_oem, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_by_model_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make** | **str**| Manufacturer slug name, use _**&#x60;GET /makes/&#x60;**_ to get possible values (e.g. &#x60;mitsubishi&#x60;) | 
 **model** | **str**| Model slug name, use _**&#x60;GET /models/&#x60;**_ to get possible values (e.g. &#x60;outlander&#x60;) | 
 **year** | **int**| You can use _**&#x60;GET /years/&#x60;**_ to get possible years (e.g. &#x60;2015&#x60;) | 
 **trim** | **str**| Use *&#x60;slug&#x60;* from _**&#x60;GET /trims/&#x60;**_ methods here. (e.g. &#x60;2.0+GG2W&#x60;) | [optional] 
 **only_oem** | **bool**| Show only original equipment wheels | [optional] 
 **lang** | **str**| Use this parameter anywhere in the API to get *&#x60;name&#x60;* field translation of the following objects: **&#x60;Make&#x60;**, **&#x60;Model&#x60;**, **&#x60;Market&#x60;**. Across the *&#x60;name&#x60;* this objects will have *&#x60;name_en&#x60;* field with original english name. By default &#x60;en&#x60; language is used.  Available languages: &#x60;en,de,ru,es,pt,fr,ja,zh-cn&#x60;. Currently translation works for chinese &#x60;zh-cn&#x60; language only | [optional] 

### Return type

[**list[Vehicle]**](Vehicle.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_rim_list**
> list[MakeWithModels] search_by_rim_list(bolt_pattern, rim_diameter, rim_width, offset=offset, offset_min=offset_min, offset_max=offset_max, cb=cb, cb_min=cb_min, cb_max=cb_max, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)

Find models matching given rim parameters

Get a list of model modifications that match the given rim parameters, grouped by manufacturer.  It's an alias for _**`GET /bolt-patterns/{bolt_pattern}/`**_        method with given path and query parameters.

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
api_instance = ws_api_client.SearchApi(ws_api_client.ApiClient(configuration))
bolt_pattern = '\"5x105\"' # str | Bolt pattern combines number of stud holes and pitch circle diameter. Use _**`GET /bolt-patterns/`**_ to get possible values (e.g. `5x105`)
rim_diameter = 16 # float | Rim diameter, in (e.g. `16`)
rim_width = 7 # float | Rim width, in (e.g. `7`)
offset = 8.14 # float | Rim offset, mm (e.g. `40`) (optional)
offset_min = 8.14 # float | Lower bound for rim offset, mm (e.g. `35`) (optional)
offset_max = 8.14 # float | Upper bound for rim offset, mm (e.g. `45`) (optional)
cb = 8.14 # float | Centre bore value, mm (e.g. `60`) (optional)
cb_min = 8.14 # float | Lower bound for centre bore value, mm (e.g. `55`) (optional)
cb_max = 8.14 # float | Upper bound for centre bore value, mm (e.g. `65`) (optional)
lang = 'lang_example' # str | Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only (optional)
brands = 'brands_example' # str | Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`) (optional)
brands_exclude = 'brands_exclude_example' # str | Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`) (optional)
countries = 'countries_example' # str | Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`) (optional)
countries_exclude = 'countries_exclude_example' # str | Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`) (optional)

try:
    # Find models matching given rim parameters
    api_response = api_instance.search_by_rim_list(bolt_pattern, rim_diameter, rim_width, offset=offset, offset_min=offset_min, offset_max=offset_max, cb=cb, cb_min=cb_min, cb_max=cb_max, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_by_rim_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bolt_pattern** | **str**| Bolt pattern combines number of stud holes and pitch circle diameter. Use _**&#x60;GET /bolt-patterns/&#x60;**_ to get possible values (e.g. &#x60;5x105&#x60;) | 
 **rim_diameter** | **float**| Rim diameter, in (e.g. &#x60;16&#x60;) | 
 **rim_width** | **float**| Rim width, in (e.g. &#x60;7&#x60;) | 
 **offset** | **float**| Rim offset, mm (e.g. &#x60;40&#x60;) | [optional] 
 **offset_min** | **float**| Lower bound for rim offset, mm (e.g. &#x60;35&#x60;) | [optional] 
 **offset_max** | **float**| Upper bound for rim offset, mm (e.g. &#x60;45&#x60;) | [optional] 
 **cb** | **float**| Centre bore value, mm (e.g. &#x60;60&#x60;) | [optional] 
 **cb_min** | **float**| Lower bound for centre bore value, mm (e.g. &#x60;55&#x60;) | [optional] 
 **cb_max** | **float**| Upper bound for centre bore value, mm (e.g. &#x60;65&#x60;) | [optional] 
 **lang** | **str**| Use this parameter anywhere in the API to get *&#x60;name&#x60;* field translation of the following objects: **&#x60;Make&#x60;**, **&#x60;Model&#x60;**, **&#x60;Market&#x60;**. Across the *&#x60;name&#x60;* this objects will have *&#x60;name_en&#x60;* field with original english name. By default &#x60;en&#x60; language is used.  Available languages: &#x60;en,de,ru,es,pt,fr,ja,zh-cn&#x60;. Currently translation works for chinese &#x60;zh-cn&#x60; language only | [optional] 
 **brands** | **str**| Show information only for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;mitsubishi,nissan,toyota&#x60;) | [optional] 
 **brands_exclude** | **str**| Don&#39;t show information for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;geely,great-wall&#x60;) | [optional] 
 **countries** | **str**| Show information for local manufacturers from specified countries only. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;us,gb,jp&#x60;) | [optional] 
 **countries_exclude** | **str**| Don&#39;t show information for local manufacturers from specified countries. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;ru,ua&#x60;) | [optional] 

### Return type

[**list[MakeWithModels]**](MakeWithModels.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_by_tire_list**
> list[MakeWithModels] search_by_tire_list(tire_width, aspect_ratio, rim_diameter, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)

Find models matching given tire parameters

Get a list of model modifications matching given tire, grouped by manufacturer.  It's an alias for _**`GET /tire/{tire}/`**_ method  (tire configuration is combined of required tire width, aspect ratio and rim diameter).

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
api_instance = ws_api_client.SearchApi(ws_api_client.ApiClient(configuration))
tire_width = 195 # float | Tire width, mm (e.g. `195`)
aspect_ratio = 50 # float | Aspect ratio, % (e.g. `50`)
rim_diameter = 16 # float | Rim diameter, in (e.g. `16`)
lang = 'lang_example' # str | Use this parameter anywhere in the API to get *`name`* field translation of the following objects: **`Make`**, **`Model`**, **`Market`**. Across the *`name`* this objects will have *`name_en`* field with original english name. By default `en` language is used.  Available languages: `en,de,ru,es,pt,fr,ja,zh-cn`. Currently translation works for chinese `zh-cn` language only (optional)
brands = 'brands_example' # str | Show information only for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `mitsubishi,nissan,toyota`) (optional)
brands_exclude = 'brands_exclude_example' # str | Don't show information for specified manufacturers. Use _**`GET /makes/`**_ method to get the full list. (e.g. `geely,great-wall`) (optional)
countries = 'countries_example' # str | Show information for local manufacturers from specified countries only. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `us,gb,jp`) (optional)
countries_exclude = 'countries_exclude_example' # str | Don't show information for local manufacturers from specified countries. Use _**`GET /countries/`**_ method to get the full list of countries. (e.g. `ru,ua`) (optional)

try:
    # Find models matching given tire parameters
    api_response = api_instance.search_by_tire_list(tire_width, aspect_ratio, rim_diameter, lang=lang, brands=brands, brands_exclude=brands_exclude, countries=countries, countries_exclude=countries_exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_by_tire_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tire_width** | **float**| Tire width, mm (e.g. &#x60;195&#x60;) | 
 **aspect_ratio** | **float**| Aspect ratio, % (e.g. &#x60;50&#x60;) | 
 **rim_diameter** | **float**| Rim diameter, in (e.g. &#x60;16&#x60;) | 
 **lang** | **str**| Use this parameter anywhere in the API to get *&#x60;name&#x60;* field translation of the following objects: **&#x60;Make&#x60;**, **&#x60;Model&#x60;**, **&#x60;Market&#x60;**. Across the *&#x60;name&#x60;* this objects will have *&#x60;name_en&#x60;* field with original english name. By default &#x60;en&#x60; language is used.  Available languages: &#x60;en,de,ru,es,pt,fr,ja,zh-cn&#x60;. Currently translation works for chinese &#x60;zh-cn&#x60; language only | [optional] 
 **brands** | **str**| Show information only for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;mitsubishi,nissan,toyota&#x60;) | [optional] 
 **brands_exclude** | **str**| Don&#39;t show information for specified manufacturers. Use _**&#x60;GET /makes/&#x60;**_ method to get the full list. (e.g. &#x60;geely,great-wall&#x60;) | [optional] 
 **countries** | **str**| Show information for local manufacturers from specified countries only. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;us,gb,jp&#x60;) | [optional] 
 **countries_exclude** | **str**| Don&#39;t show information for local manufacturers from specified countries. Use _**&#x60;GET /countries/&#x60;**_ method to get the full list of countries. (e.g. &#x60;ru,ua&#x60;) | [optional] 

### Return type

[**list[MakeWithModels]**](MakeWithModels.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

