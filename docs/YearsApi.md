# ws_api_client.YearsApi

All URIs are relative to *https://api.wheel-size.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**years_list**](YearsApi.md#years_list) | **GET** /years/ | Returns list of years for the given manufacturer/model


# **years_list**
> list[Year] years_list(make, model=model)

Returns list of years for the given manufacturer/model

Get a list of years that match the given manufacturer and model (if present)

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
api_instance = ws_api_client.YearsApi(ws_api_client.ApiClient(configuration))
make = '\"mitsubishi\"' # str | Manufacturer slug name, use _**`GET /makes/`**_ to get possible values (e.g. `mitsubishi`)
model = 'model_example' # str | Model slug name, use _**`GET /models/`**_ to get possible values (e.g. `outlander`) (optional)

try:
    # Returns list of years for the given manufacturer/model
    api_response = api_instance.years_list(make, model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearsApi->years_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **make** | **str**| Manufacturer slug name, use _**&#x60;GET /makes/&#x60;**_ to get possible values (e.g. &#x60;mitsubishi&#x60;) | 
 **model** | **str**| Model slug name, use _**&#x60;GET /models/&#x60;**_ to get possible values (e.g. &#x60;outlander&#x60;) | [optional] 

### Return type

[**list[Year]**](Year.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

