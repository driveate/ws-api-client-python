# swagger_client.CountriesApi

All URIs are relative to *https://api.wheel-size.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countries_list**](CountriesApi.md#countries_list) | **GET** /countries/ | Returns a list of countries


# **countries_list**
> list[Country] countries_list()

Returns a list of countries

List of possible countries to be used in any other API method. Indended to be used in case you want to restrict results for several countries.

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
api_instance = swagger_client.CountriesApi(swagger_client.ApiClient(configuration))

try:
    # Returns a list of countries
    api_response = api_instance.countries_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->countries_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Country]**](Country.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

