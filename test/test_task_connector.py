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

from __future__ import absolute_import

import os
import sys
import unittest

import ProcessMaker_PMIO
from ProcessMaker_PMIO.rest import ApiException
from ProcessMaker_PMIO.models.task_connector import TaskConnector


class TestTaskConnector(unittest.TestCase):
    """ TaskConnector unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskConnector(self):
        """
        Test TaskConnector
        """
        model = ProcessMaker_PMIO.models.task_connector.TaskConnector()


if __name__ == '__main__':
    unittest.main()
