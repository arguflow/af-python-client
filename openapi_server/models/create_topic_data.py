from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class CreateTopicData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, normal_chat=None, resolution=None):  # noqa: E501
        """CreateTopicData - a model defined in OpenAPI

        :param normal_chat: The normal_chat of this CreateTopicData.  # noqa: E501
        :type normal_chat: bool
        :param resolution: The resolution of this CreateTopicData.  # noqa: E501
        :type resolution: str
        """
        self.openapi_types = {
            'normal_chat': bool,
            'resolution': str
        }

        self.attribute_map = {
            'normal_chat': 'normal_chat',
            'resolution': 'resolution'
        }

        self._normal_chat = normal_chat
        self._resolution = resolution

    @classmethod
    def from_dict(cls, dikt) -> 'CreateTopicData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateTopicData of this CreateTopicData.  # noqa: E501
        :rtype: CreateTopicData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def normal_chat(self) -> bool:
        """Gets the normal_chat of this CreateTopicData.


        :return: The normal_chat of this CreateTopicData.
        :rtype: bool
        """
        return self._normal_chat

    @normal_chat.setter
    def normal_chat(self, normal_chat: bool):
        """Sets the normal_chat of this CreateTopicData.


        :param normal_chat: The normal_chat of this CreateTopicData.
        :type normal_chat: bool
        """

        self._normal_chat = normal_chat

    @property
    def resolution(self) -> str:
        """Gets the resolution of this CreateTopicData.


        :return: The resolution of this CreateTopicData.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: str):
        """Sets the resolution of this CreateTopicData.


        :param resolution: The resolution of this CreateTopicData.
        :type resolution: str
        """
        if resolution is None:
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution
