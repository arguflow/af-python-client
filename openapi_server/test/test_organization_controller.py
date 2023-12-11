import unittest

from flask import json

from openapi_server.models.create_organization_data import CreateOrganizationData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.models.update_organization_data import UpdateOrganizationData  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrganizationController(BaseTestCase):
    """OrganizationController integration test stubs"""

    def test_create_organization(self):
        """Test case for create_organization

        
        """
        create_organization_data = {"configuration":"","name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/organization',
            method='POST',
            headers=headers,
            data=json.dumps(create_organization_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_organization_by_id(self):
        """Test case for delete_organization_by_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/organization/{organization_id}'.format(organization_id='organization_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_organization_by_id(self):
        """Test case for get_organization_by_id

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/organization/{organization_id}'.format(organization_id='organization_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_organization(self):
        """Test case for update_organization

        
        """
        update_organization_data = {"configuration":"","organization_uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/organization',
            method='PUT',
            headers=headers,
            data=json.dumps(update_organization_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
