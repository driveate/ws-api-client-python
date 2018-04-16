# coding: utf-8

# flake8: noqa

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from ws_api_client.api.bolt_patterns_api import BoltPatternsApi
from ws_api_client.api.countries_api import CountriesApi
from ws_api_client.api.generations_api import GenerationsApi
from ws_api_client.api.makes_api import MakesApi
from ws_api_client.api.markets_api import MarketsApi
from ws_api_client.api.models_api import ModelsApi
from ws_api_client.api.search_api import SearchApi
from ws_api_client.api.tires_api import TiresApi
from ws_api_client.api.trims_api import TrimsApi
from ws_api_client.api.vehicles_api import VehiclesApi
from ws_api_client.api.years_api import YearsApi

# import ApiClient
from ws_api_client.api_client import ApiClient
from ws_api_client.configuration import Configuration
# import models into sdk package
from ws_api_client.models.aggregation import Aggregation
from ws_api_client.models.body import Body
from ws_api_client.models.bolt_pattern import BoltPattern
from ws_api_client.models.country import Country
from ws_api_client.models.generation import Generation
from ws_api_client.models.make_model import MakeModel
from ws_api_client.models.make_with_models import MakeWithModels
from ws_api_client.models.market import Market
from ws_api_client.models.model import Model
from ws_api_client.models.model_with_tires import ModelWithTires
from ws_api_client.models.model_with_trims import ModelWithTrims
from ws_api_client.models.power import Power
from ws_api_client.models.pressure import Pressure
from ws_api_client.models.rim_agregation import RimAgregation
from ws_api_client.models.size_aggregation import SizeAggregation
from ws_api_client.models.tire import Tire
from ws_api_client.models.tires_aggregation import TiresAggregation
from ws_api_client.models.trim import Trim
from ws_api_client.models.trim_with_market_and_years import TrimWithMarketAndYears
from ws_api_client.models.vehicle import Vehicle
from ws_api_client.models.wheel import Wheel
from ws_api_client.models.wheel_pair import WheelPair
from ws_api_client.models.year import Year
