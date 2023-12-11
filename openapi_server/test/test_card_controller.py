import unittest

from flask import json

from openapi_server.models.card_metadata import CardMetadata  # noqa: E501
from openapi_server.models.card_metadata_with_file_data import CardMetadataWithFileData  # noqa: E501
from openapi_server.models.create_card_data import CreateCardData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.generate_cards_request import GenerateCardsRequest  # noqa: E501
from openapi_server.models.recommend_cards_request import RecommendCardsRequest  # noqa: E501
from openapi_server.models.return_created_card import ReturnCreatedCard  # noqa: E501
from openapi_server.models.search_card_data import SearchCardData  # noqa: E501
from openapi_server.models.search_card_query_response_body import SearchCardQueryResponseBody  # noqa: E501
from openapi_server.models.suggested_queries_request import SuggestedQueriesRequest  # noqa: E501
from openapi_server.models.suggested_queries_response import SuggestedQueriesResponse  # noqa: E501
from openapi_server.models.update_card_by_tracking_id_data import UpdateCardByTrackingIdData  # noqa: E501
from openapi_server.models.update_card_data import UpdateCardData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCardController(BaseTestCase):
    """CardController integration test stubs"""

    def test_create_card(self):
        """Test case for create_card

        
        """
        create_card_data = {"collection_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","metadata":"","private":True,"time_stamp":"time_stamp","card_html":"card_html","file_uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","link":"link","tag_set":"tag_set","tracking_id":"tracking_id","card_vector":[0.8008282,0.8008282]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card',
            method='POST',
            headers=headers,
            data=json.dumps(create_card_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_suggested_queries_handler(self):
        """Test case for create_suggested_queries_handler

        
        """
        suggested_queries_request = {"query":"query"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/gen_suggestions',
            method='POST',
            headers=headers,
            data=json.dumps(suggested_queries_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_card(self):
        """Test case for delete_card

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/card/{card_id}'.format(card_id='card_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_card_by_tracking_id(self):
        """Test case for delete_card_by_tracking_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/card/tracking_id/{tracking_id}'.format(tracking_id='tracking_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generate_off_cards(self):
        """Test case for generate_off_cards

        
        """
        generate_cards_request = {"prev_messages":[{"role":"role","name":"name","content":"content"},{"role":"role","name":"name","content":"content"}],"card_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/generate',
            method='POST',
            headers=headers,
            data=json.dumps(generate_cards_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_card_by_tracking_id(self):
        """Test case for get_card_by_tracking_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/card/tracking_id/{tracking_id}'.format(tracking_id='tracking_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recommended_cards(self):
        """Test case for get_recommended_cards

        
        """
        recommend_cards_request = {"positive_card_ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/recommend',
            method='POST',
            headers=headers,
            data=json.dumps(recommend_cards_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_card(self):
        """Test case for search_card

        
        """
        search_card_data = {"cross_encoder":True,"time_range":[null,null],"link":["link","link"],"filters":"","tag_set":["tag_set","tag_set"],"weights":[null,null],"search_type":"search_type","content":"content"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/search'.format(page=56),
            method='POST',
            headers=headers,
            data=json.dumps(search_card_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_card(self):
        """Test case for update_card

        
        """
        update_card_data = {"metadata":"","private":True,"time_stamp":"time_stamp","card_html":"card_html","link":"link","tracking_id":"tracking_id","card_uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/update',
            method='PUT',
            headers=headers,
            data=json.dumps(update_card_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_card_by_tracking_id(self):
        """Test case for update_card_by_tracking_id

        
        """
        update_card_by_tracking_id_data = {"metadata":"","private":True,"time_stamp":"time_stamp","card_html":"card_html","link":"link","tracking_id":"tracking_id","card_uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/card/tracking_id/update',
            method='PUT',
            headers=headers,
            data=json.dumps(update_card_by_tracking_id_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
