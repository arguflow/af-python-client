import unittest

from flask import json

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.notification_id import NotificationId  # noqa: E501
from openapi_server.models.notification_return import NotificationReturn  # noqa: E501
from openapi_server.test import BaseTestCase


class TestNotificationsController(BaseTestCase):
    """NotificationsController integration test stubs"""

    def test_get_notifications(self):
        """Test case for get_notifications

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/notifications/{page}'.format(page=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mark_all_notifications_as_read(self):
        """Test case for mark_all_notifications_as_read

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/notifications_readall',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mark_notification_as_read(self):
        """Test case for mark_notification_as_read

        
        """
        notification_id = {"notification_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/notifications',
            method='PUT',
            headers=headers,
            data=json.dumps(notification_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
