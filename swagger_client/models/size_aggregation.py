# coding: utf-8

"""
    Wheel Fitment API

    The Wheel Fitment API allows for programmatic access to the database of www.wheel-size.com and its services. Use this API to retrieve information about vehicle fitment database for rims and tires, including OE and option fitments, and plus/minus sizing fitment information. A variety of country and language specific options are available. The coverage of fitment data for vehicles manufactured since 2000 is nearly 100%.  The information about fitment data is updated on a daily basis.  # noqa: E501

    OpenAPI spec version: v1
    Contact: info@wheel-size.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SizeAggregation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'min': 'float',
        'max': 'float'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, min=None, max=None):  # noqa: E501
        """SizeAggregation - a model defined in Swagger"""  # noqa: E501

        self._min = None
        self._max = None
        self.discriminator = None

        self.min = min
        self.max = max

    @property
    def min(self):
        """Gets the min of this SizeAggregation.  # noqa: E501

        Size combined from minimum *`width`*, *`aspect_ratio`* and *`diameter`*  # noqa: E501

        :return: The min of this SizeAggregation.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this SizeAggregation.

        Size combined from minimum *`width`*, *`aspect_ratio`* and *`diameter`*  # noqa: E501

        :param min: The min of this SizeAggregation.  # noqa: E501
        :type: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self):
        """Gets the max of this SizeAggregation.  # noqa: E501

        Size combined from maximum *`width`*, *`aspect_ratio`* and *`diameter`*  # noqa: E501

        :return: The max of this SizeAggregation.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this SizeAggregation.

        Size combined from maximum *`width`*, *`aspect_ratio`* and *`diameter`*  # noqa: E501

        :param max: The max of this SizeAggregation.  # noqa: E501
        :type: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SizeAggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other