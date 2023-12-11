import unittest

from flask import json

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.file_dto import FileDTO  # noqa: E501
from openapi_server.models.update_file_data import UpdateFileData  # noqa: E501
from openapi_server.models.upload_file_data import UploadFileData  # noqa: E501
from openapi_server.models.upload_file_result import UploadFileResult  # noqa: E501
from openapi_server.test import BaseTestCase


class TestFileController(BaseTestCase):
    """FileController integration test stubs"""

    def test_delete_file_handler(self):
        """Test case for delete_file_handler

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/file/{file_id}'.format(file_id='file_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_file_handler(self):
        """Test case for get_file_handler

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/file/{file_id}'.format(file_id='file_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_image_file(self):
        """Test case for get_image_file

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/image/{file_name}'.format(file_name='file_name_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_file_handler(self):
        """Test case for update_file_handler

        
        """
        update_file_data = {"private":True,"file_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/file',
            method='PUT',
            headers=headers,
            data=json.dumps(update_file_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_file_handler(self):
        """Test case for upload_file_handler

        
        """
        upload_file_data = {"metadata":"","private":True,"time_stamp":"time_stamp","file_name":"file_name","link":"link","base64_docx_file":"base64_docx_file","description":"description","file_mime_type":"file_mime_type","tag_set":"tag_set","create_cards":True}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/file',
            method='POST',
            headers=headers,
            data=json.dumps(upload_file_data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
