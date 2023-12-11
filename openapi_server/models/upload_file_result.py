from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.file import File
from openapi_server import util

from openapi_server.models.file import File  # noqa: E501

class UploadFileResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_metadata=None):  # noqa: E501
        """UploadFileResult - a model defined in OpenAPI

        :param file_metadata: The file_metadata of this UploadFileResult.  # noqa: E501
        :type file_metadata: File
        """
        self.openapi_types = {
            'file_metadata': File
        }

        self.attribute_map = {
            'file_metadata': 'file_metadata'
        }

        self._file_metadata = file_metadata

    @classmethod
    def from_dict(cls, dikt) -> 'UploadFileResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UploadFileResult of this UploadFileResult.  # noqa: E501
        :rtype: UploadFileResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_metadata(self) -> File:
        """Gets the file_metadata of this UploadFileResult.


        :return: The file_metadata of this UploadFileResult.
        :rtype: File
        """
        return self._file_metadata

    @file_metadata.setter
    def file_metadata(self, file_metadata: File):
        """Sets the file_metadata of this UploadFileResult.


        :param file_metadata: The file_metadata of this UploadFileResult.
        :type file_metadata: File
        """
        if file_metadata is None:
            raise ValueError("Invalid value for `file_metadata`, must not be `None`")  # noqa: E501

        self._file_metadata = file_metadata
