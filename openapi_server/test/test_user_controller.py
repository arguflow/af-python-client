import unittest

from flask import json

from openapi_server.models.collection_data import CollectionData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.file import File  # noqa: E501
from openapi_server.models.set_user_api_key_response import SetUserApiKeyResponse  # noqa: E501
from openapi_server.models.slim_user import SlimUser  # noqa: E501
from openapi_server.models.update_user_data import UpdateUserData  # noqa: E501
from openapi_server.models.user_dto_with_cards import UserDTOWithCards  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_get_specific_user_card_collections(self):
        """Test case for get_specific_user_card_collections

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/user/collections/{user_id}/{page}'.format(user_id='user_id_example', page=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_files_handler(self):
        """Test case for get_user_files_handler

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/user/files/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_with_cards_by_id(self):
        """Test case for get_user_with_cards_by_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/user/{user_id}/{page}'.format(user_id='user_id_example', page=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_user_api_key(self):
        """Test case for set_user_api_key

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/user/set_api_key',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        
        """
        update_user_data = {"website":"website","visible_email":True,"username":"username"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/user',
            method='PUT',
            headers=headers,
            data=json.dumps(update_user_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
