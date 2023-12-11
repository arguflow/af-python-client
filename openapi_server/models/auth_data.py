from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class AuthData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, password=None):  # noqa: E501
        """AuthData - a model defined in OpenAPI

        :param email: The email of this AuthData.  # noqa: E501
        :type email: str
        :param password: The password of this AuthData.  # noqa: E501
        :type password: str
        """
        self.openapi_types = {
            'email': str,
            'password': str
        }

        self.attribute_map = {
            'email': 'email',
            'password': 'password'
        }

        self._email = email
        self._password = password

    @classmethod
    def from_dict(cls, dikt) -> 'AuthData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AuthData of this AuthData.  # noqa: E501
        :rtype: AuthData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this AuthData.


        :return: The email of this AuthData.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this AuthData.


        :param email: The email of this AuthData.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self) -> str:
        """Gets the password of this AuthData.


        :return: The password of this AuthData.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password: str):
        """Sets the password of this AuthData.


        :param password: The password of this AuthData.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password
