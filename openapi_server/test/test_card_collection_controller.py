import unittest

from flask import json

from openapi_server.models.add_card_to_collection_data import AddCardToCollectionData  # noqa: E501
from openapi_server.models.bookmark_data import BookmarkData  # noqa: E501
from openapi_server.models.card_collection import CardCollection  # noqa: E501
from openapi_server.models.collection_data import CollectionData  # noqa: E501
from openapi_server.models.create_card_collection_data import CreateCardCollectionData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.delete_collection_data import DeleteCollectionData  # noqa: E501
from openapi_server.models.remove_bookmark_data import RemoveBookmarkData  # noqa: E501
from openapi_server.models.update_card_collection_data import UpdateCardCollectionData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCardCollectionController(BaseTestCase):
    """CardCollectionController integration test stubs"""

    def test_add_bookmark(self):
        """Test case for add_bookmark

        
        """
        add_card_to_collection_data = {"card_metadata_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection/{page_or_card_collection_id}'.format(page_or_card_collection_id='page_or_card_collection_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(add_card_to_collection_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_card_collection(self):
        """Test case for create_card_collection

        
        """
        create_card_collection_data = {"is_public":True,"name":"name","description":"description"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection',
            method='POST',
            headers=headers,
            data=json.dumps(create_card_collection_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_bookmark(self):
        """Test case for delete_bookmark

        
        """
        remove_bookmark_data = {"card_metadata_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection/{page_or_card_collection_id}'.format(page_or_card_collection_id='page_or_card_collection_id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(remove_bookmark_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_card_collection(self):
        """Test case for delete_card_collection

        
        """
        delete_collection_data = {"collection_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection',
            method='DELETE',
            headers=headers,
            data=json.dumps(delete_collection_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_bookmarks(self):
        """Test case for get_all_bookmarks

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection/{collection_id}/{page}'.format(collection_id='collection_id_example', page=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_logged_in_user_card_collections(self):
        """Test case for get_logged_in_user_card_collections

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection/{page_or_card_collection_id}'.format(page_or_card_collection_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_card_collection(self):
        """Test case for update_card_collection

        
        """
        update_card_collection_data = {"collection_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","is_public":True,"name":"name","description":"description"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card_collection',
            method='PUT',
            headers=headers,
            data=json.dumps(update_card_collection_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
