from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateUserData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, visible_email=None, website=None):  # noqa: E501
        """UpdateUserData - a model defined in OpenAPI

        :param username: The username of this UpdateUserData.  # noqa: E501
        :type username: str
        :param visible_email: The visible_email of this UpdateUserData.  # noqa: E501
        :type visible_email: bool
        :param website: The website of this UpdateUserData.  # noqa: E501
        :type website: str
        """
        self.openapi_types = {
            'username': str,
            'visible_email': bool,
            'website': str
        }

        self.attribute_map = {
            'username': 'username',
            'visible_email': 'visible_email',
            'website': 'website'
        }

        self._username = username
        self._visible_email = visible_email
        self._website = website

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateUserData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateUserData of this UpdateUserData.  # noqa: E501
        :rtype: UpdateUserData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self) -> str:
        """Gets the username of this UpdateUserData.


        :return: The username of this UpdateUserData.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this UpdateUserData.


        :param username: The username of this UpdateUserData.
        :type username: str
        """

        self._username = username

    @property
    def visible_email(self) -> bool:
        """Gets the visible_email of this UpdateUserData.


        :return: The visible_email of this UpdateUserData.
        :rtype: bool
        """
        return self._visible_email

    @visible_email.setter
    def visible_email(self, visible_email: bool):
        """Sets the visible_email of this UpdateUserData.


        :param visible_email: The visible_email of this UpdateUserData.
        :type visible_email: bool
        """
        if visible_email is None:
            raise ValueError("Invalid value for `visible_email`, must not be `None`")  # noqa: E501

        self._visible_email = visible_email

    @property
    def website(self) -> str:
        """Gets the website of this UpdateUserData.


        :return: The website of this UpdateUserData.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this UpdateUserData.


        :param website: The website of this UpdateUserData.
        :type website: str
        """

        self._website = website
