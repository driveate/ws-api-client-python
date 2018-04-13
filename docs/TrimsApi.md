# swagger_client.TrimsApi

All URIs are relative to *https://api.wheel-size.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trims_list**](TrimsApi.md#trims_list) | **GET** /trims/ | Model modifications


# **trims_list**
> list[Trim] trims_list(make, model, year)

Model modifications

List of model modifications matching given manufacturer, model and year

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: user_key
configuration = swagger_client.Configuration()
configuration.api_key['user_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TrimsApi(swagger_client.ApiClient(configuration))
make = 'make_example' # str | Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`)
model = 'model_example' # str | Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`)
year = 56 # int | You can use _**`GET /years/`**_ to get possible years (e.g. `2015`)

try:
    # Model modifications
    api_response = api_instance.trims_list(make, model, year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrimsApi->trims_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make** | **str**| Manufacturer slug name, use _**&#x60;GET /makes/&#x60;**_ to get possible values (e.g. &#x60;mitsubishi&#x60;) | 
 **model** | **str**| Model slug name, use _**&#x60;GET /models/&#x60;**_ to get possible values (e.g. &#x60;outlander&#x60;) | 
 **year** | **int**| You can use _**&#x60;GET /years/&#x60;**_ to get possible years (e.g. &#x60;2015&#x60;) | 

### Return type

[**list[Trim]**](Trim.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

