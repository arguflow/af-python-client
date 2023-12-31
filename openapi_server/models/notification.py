from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.file_upload_completed_notification_with_name import FileUploadCompletedNotificationWithName
from openapi_server import util

from openapi_server.models.file_upload_completed_notification_with_name import FileUploadCompletedNotificationWithName  # noqa: E501

class Notification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, collection_name=None, collection_uuid=None, created_at=None, id=None, updated_at=None, user_read=None, user_uuid=None):  # noqa: E501
        """Notification - a model defined in OpenAPI

        :param collection_name: The collection_name of this Notification.  # noqa: E501
        :type collection_name: str
        :param collection_uuid: The collection_uuid of this Notification.  # noqa: E501
        :type collection_uuid: str
        :param created_at: The created_at of this Notification.  # noqa: E501
        :type created_at: datetime
        :param id: The id of this Notification.  # noqa: E501
        :type id: str
        :param updated_at: The updated_at of this Notification.  # noqa: E501
        :type updated_at: datetime
        :param user_read: The user_read of this Notification.  # noqa: E501
        :type user_read: bool
        :param user_uuid: The user_uuid of this Notification.  # noqa: E501
        :type user_uuid: str
        """
        self.openapi_types = {
            'collection_name': str,
            'collection_uuid': str,
            'created_at': datetime,
            'id': str,
            'updated_at': datetime,
            'user_read': bool,
            'user_uuid': str
        }

        self.attribute_map = {
            'collection_name': 'collection_name',
            'collection_uuid': 'collection_uuid',
            'created_at': 'created_at',
            'id': 'id',
            'updated_at': 'updated_at',
            'user_read': 'user_read',
            'user_uuid': 'user_uuid'
        }

        self._collection_name = collection_name
        self._collection_uuid = collection_uuid
        self._created_at = created_at
        self._id = id
        self._updated_at = updated_at
        self._user_read = user_read
        self._user_uuid = user_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Notification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Notification of this Notification.  # noqa: E501
        :rtype: Notification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def collection_name(self) -> str:
        """Gets the collection_name of this Notification.


        :return: The collection_name of this Notification.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name: str):
        """Sets the collection_name of this Notification.


        :param collection_name: The collection_name of this Notification.
        :type collection_name: str
        """

        self._collection_name = collection_name

    @property
    def collection_uuid(self) -> str:
        """Gets the collection_uuid of this Notification.


        :return: The collection_uuid of this Notification.
        :rtype: str
        """
        return self._collection_uuid

    @collection_uuid.setter
    def collection_uuid(self, collection_uuid: str):
        """Sets the collection_uuid of this Notification.


        :param collection_uuid: The collection_uuid of this Notification.
        :type collection_uuid: str
        """
        if collection_uuid is None:
            raise ValueError("Invalid value for `collection_uuid`, must not be `None`")  # noqa: E501

        self._collection_uuid = collection_uuid

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this Notification.


        :return: The created_at of this Notification.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this Notification.


        :param created_at: The created_at of this Notification.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self) -> str:
        """Gets the id of this Notification.


        :return: The id of this Notification.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Notification.


        :param id: The id of this Notification.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this Notification.


        :return: The updated_at of this Notification.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this Notification.


        :param updated_at: The updated_at of this Notification.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_read(self) -> bool:
        """Gets the user_read of this Notification.


        :return: The user_read of this Notification.
        :rtype: bool
        """
        return self._user_read

    @user_read.setter
    def user_read(self, user_read: bool):
        """Sets the user_read of this Notification.


        :param user_read: The user_read of this Notification.
        :type user_read: bool
        """
        if user_read is None:
            raise ValueError("Invalid value for `user_read`, must not be `None`")  # noqa: E501

        self._user_read = user_read

    @property
    def user_uuid(self) -> str:
        """Gets the user_uuid of this Notification.


        :return: The user_uuid of this Notification.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid: str):
        """Sets the user_uuid of this Notification.


        :param user_uuid: The user_uuid of this Notification.
        :type user_uuid: str
        """
        if user_uuid is None:
            raise ValueError("Invalid value for `user_uuid`, must not be `None`")  # noqa: E501

        self._user_uuid = user_uuid
