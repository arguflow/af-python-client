import unittest

from flask import json

from openapi_server.models.create_message_data import CreateMessageData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.edit_message_data import EditMessageData  # noqa: E501
from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.regenerate_message_data import RegenerateMessageData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_create_message_completion_handler(self):
        """Test case for create_message_completion_handler

        
        """
        create_message_data = {"topic_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","new_message_content":"new_message_content"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/message',
            method='POST',
            headers=headers,
            data=json.dumps(create_message_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_message_handler(self):
        """Test case for edit_message_handler

        
        """
        edit_message_data = {"message_sort_order":0,"topic_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","new_message_content":"new_message_content"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/message',
            method='PUT',
            headers=headers,
            data=json.dumps(edit_message_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_topic_messages(self):
        """Test case for get_all_topic_messages

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/messages/{messages_topic_id}'.format(messages_topic_id='messages_topic_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regenerate_message_handler(self):
        """Test case for regenerate_message_handler

        
        """
        regenerate_message_data = {"topic_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/message',
            method='DELETE',
            headers=headers,
            data=json.dumps(regenerate_message_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
