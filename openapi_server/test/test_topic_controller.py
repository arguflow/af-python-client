import unittest

from flask import json

from openapi_server.models.create_topic_data import CreateTopicData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.delete_topic_data import DeleteTopicData  # noqa: E501
from openapi_server.models.topic import Topic  # noqa: E501
from openapi_server.models.update_topic_data import UpdateTopicData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTopicController(BaseTestCase):
    """TopicController integration test stubs"""

    def test_create_topic(self):
        """Test case for create_topic

        
        """
        create_topic_data = {"normal_chat":True,"resolution":"resolution"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/topic',
            method='POST',
            headers=headers,
            data=json.dumps(create_topic_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_topic(self):
        """Test case for delete_topic

        
        """
        delete_topic_data = {"topic_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/topic',
            method='DELETE',
            headers=headers,
            data=json.dumps(delete_topic_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_topics(self):
        """Test case for get_all_topics

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/topic',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_topic(self):
        """Test case for update_topic

        
        """
        update_topic_data = {"side":True,"topic_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","resolution":"resolution"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/topic',
            method='PUT',
            headers=headers,
            data=json.dumps(update_topic_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
