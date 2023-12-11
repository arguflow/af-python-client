import unittest

from flask import json

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.test import BaseTestCase


class TestHealthController(BaseTestCase):
    """HealthController integration test stubs"""

    def test_health_check(self):
        """Test case for health_check

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/health',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
