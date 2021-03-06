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


class FlowAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, process_id=None, from_object_id=None, from_object_type=None, to_object_id=None, to_object_type=None, type='SEQUENTIAL', condition=None, default=False, optional=False, created_at=None, updated_at=None):
        """
        FlowAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'process_id': 'str',
            'from_object_id': 'str',
            'from_object_type': 'str',
            'to_object_id': 'str',
            'to_object_type': 'str',
            'type': 'str',
            'condition': 'str',
            'default': 'bool',
            'optional': 'bool',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'process_id': 'process_id',
            'from_object_id': 'from_object_id',
            'from_object_type': 'from_object_type',
            'to_object_id': 'to_object_id',
            'to_object_type': 'to_object_type',
            'type': 'type',
            'condition': 'condition',
            'default': 'default',
            'optional': 'optional',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._name = name
        self._description = description
        self._process_id = process_id
        self._from_object_id = from_object_id
        self._from_object_type = from_object_type
        self._to_object_id = to_object_id
        self._to_object_type = to_object_type
        self._type = type
        self._condition = condition
        self._default = default
        self._optional = optional
        self._created_at = created_at
        self._updated_at = updated_at


    @property
    def name(self):
        """
        Gets the name of this FlowAttributes.


        :return: The name of this FlowAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FlowAttributes.


        :param name: The name of this FlowAttributes.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FlowAttributes.


        :return: The description of this FlowAttributes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FlowAttributes.


        :param description: The description of this FlowAttributes.
        :type: str
        """

        self._description = description

    @property
    def process_id(self):
        """
        Gets the process_id of this FlowAttributes.


        :return: The process_id of this FlowAttributes.
        :rtype: str
        """
        return self._process_id

    @process_id.setter
    def process_id(self, process_id):
        """
        Sets the process_id of this FlowAttributes.


        :param process_id: The process_id of this FlowAttributes.
        :type: str
        """

        self._process_id = process_id

    @property
    def from_object_id(self):
        """
        Gets the from_object_id of this FlowAttributes.


        :return: The from_object_id of this FlowAttributes.
        :rtype: str
        """
        return self._from_object_id

    @from_object_id.setter
    def from_object_id(self, from_object_id):
        """
        Sets the from_object_id of this FlowAttributes.


        :param from_object_id: The from_object_id of this FlowAttributes.
        :type: str
        """

        self._from_object_id = from_object_id

    @property
    def from_object_type(self):
        """
        Gets the from_object_type of this FlowAttributes.


        :return: The from_object_type of this FlowAttributes.
        :rtype: str
        """
        return self._from_object_type

    @from_object_type.setter
    def from_object_type(self, from_object_type):
        """
        Sets the from_object_type of this FlowAttributes.


        :param from_object_type: The from_object_type of this FlowAttributes.
        :type: str
        """

        self._from_object_type = from_object_type

    @property
    def to_object_id(self):
        """
        Gets the to_object_id of this FlowAttributes.


        :return: The to_object_id of this FlowAttributes.
        :rtype: str
        """
        return self._to_object_id

    @to_object_id.setter
    def to_object_id(self, to_object_id):
        """
        Sets the to_object_id of this FlowAttributes.


        :param to_object_id: The to_object_id of this FlowAttributes.
        :type: str
        """

        self._to_object_id = to_object_id

    @property
    def to_object_type(self):
        """
        Gets the to_object_type of this FlowAttributes.


        :return: The to_object_type of this FlowAttributes.
        :rtype: str
        """
        return self._to_object_type

    @to_object_type.setter
    def to_object_type(self, to_object_type):
        """
        Sets the to_object_type of this FlowAttributes.


        :param to_object_type: The to_object_type of this FlowAttributes.
        :type: str
        """

        self._to_object_type = to_object_type

    @property
    def type(self):
        """
        Gets the type of this FlowAttributes.


        :return: The type of this FlowAttributes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FlowAttributes.


        :param type: The type of this FlowAttributes.
        :type: str
        """
        allowed_values = ["SEQUENTIAL", "EVALUATE", "SELECT", "PARALLEL", "PARALLEL-BY-EVALUATION", "SEC-JOIN", "DISCRIMINATOR"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def condition(self):
        """
        Gets the condition of this FlowAttributes.


        :return: The condition of this FlowAttributes.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this FlowAttributes.


        :param condition: The condition of this FlowAttributes.
        :type: str
        """

        self._condition = condition

    @property
    def default(self):
        """
        Gets the default of this FlowAttributes.


        :return: The default of this FlowAttributes.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this FlowAttributes.


        :param default: The default of this FlowAttributes.
        :type: bool
        """

        self._default = default

    @property
    def optional(self):
        """
        Gets the optional of this FlowAttributes.


        :return: The optional of this FlowAttributes.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this FlowAttributes.


        :param optional: The optional of this FlowAttributes.
        :type: bool
        """

        self._optional = optional

    @property
    def created_at(self):
        """
        Gets the created_at of this FlowAttributes.


        :return: The created_at of this FlowAttributes.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FlowAttributes.


        :param created_at: The created_at of this FlowAttributes.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this FlowAttributes.


        :return: The updated_at of this FlowAttributes.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this FlowAttributes.


        :param updated_at: The updated_at of this FlowAttributes.
        :type: str
        """

        self._updated_at = updated_at

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
