import unittest

from flask import json

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.slim_user import SlimUser  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_get_me(self):
        """Test case for get_me

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/auth',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login(self):
        """Test case for login

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/auth',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout(self):
        """Test case for logout

        
        """
        headers = { 
        }
        response = self.client.open(
            '/api/auth',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
