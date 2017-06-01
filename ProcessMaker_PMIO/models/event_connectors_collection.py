# coding: utf-8

"""
    ProcessMaker API

    This ProcessMaker I/O API provides access to a BPMN 2.0 compliant workflow engine api that is designed to be used as a microservice to support enterprise cloud applications.  The current Alpha 1.0 version supports most of the descriptive class of the BPMN 2.0 specification.

    OpenAPI spec version: 1.0.0
    Contact: support@processmaker.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class EventConnectorsCollection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data=None, meta=None):
        """
        EventConnectorsCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data': 'list[EventConnector]',
            'meta': 'Meta'
        }

        self.attribute_map = {
            'data': 'data',
            'meta': 'meta'
        }

        self._data = data
        self._meta = meta


    @property
    def data(self):
        """
        Gets the data of this EventConnectorsCollection.


        :return: The data of this EventConnectorsCollection.
        :rtype: list[EventConnector]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this EventConnectorsCollection.


        :param data: The data of this EventConnectorsCollection.
        :type: list[EventConnector]
        """

        self._data = data

    @property
    def meta(self):
        """
        Gets the meta of this EventConnectorsCollection.


        :return: The meta of this EventConnectorsCollection.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this EventConnectorsCollection.


        :param meta: The meta of this EventConnectorsCollection.
        :type: Meta
        """

        self._meta = meta

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other