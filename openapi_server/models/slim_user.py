from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class SlimUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email=None, id=None, organization_id=None, username=None, visible_email=None, website=None):  # noqa: E501
        """SlimUser - a model defined in OpenAPI

        :param email: The email of this SlimUser.  # noqa: E501
        :type email: str
        :param id: The id of this SlimUser.  # noqa: E501
        :type id: str
        :param organization_id: The organization_id of this SlimUser.  # noqa: E501
        :type organization_id: str
        :param username: The username of this SlimUser.  # noqa: E501
        :type username: str
        :param visible_email: The visible_email of this SlimUser.  # noqa: E501
        :type visible_email: bool
        :param website: The website of this SlimUser.  # noqa: E501
        :type website: str
        """
        self.openapi_types = {
            'email': str,
            'id': str,
            'organization_id': str,
            'username': str,
            'visible_email': bool,
            'website': str
        }

        self.attribute_map = {
            'email': 'email',
            'id': 'id',
            'organization_id': 'organization_id',
            'username': 'username',
            'visible_email': 'visible_email',
            'website': 'website'
        }

        self._email = email
        self._id = id
        self._organization_id = organization_id
        self._username = username
        self._visible_email = visible_email
        self._website = website

    @classmethod
    def from_dict(cls, dikt) -> 'SlimUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SlimUser of this SlimUser.  # noqa: E501
        :rtype: SlimUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self) -> str:
        """Gets the email of this SlimUser.


        :return: The email of this SlimUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this SlimUser.


        :param email: The email of this SlimUser.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def id(self) -> str:
        """Gets the id of this SlimUser.


        :return: The id of this SlimUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this SlimUser.


        :param id: The id of this SlimUser.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def organization_id(self) -> str:
        """Gets the organization_id of this SlimUser.


        :return: The organization_id of this SlimUser.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: str):
        """Sets the organization_id of this SlimUser.


        :param organization_id: The organization_id of this SlimUser.
        :type organization_id: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def username(self) -> str:
        """Gets the username of this SlimUser.


        :return: The username of this SlimUser.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this SlimUser.


        :param username: The username of this SlimUser.
        :type username: str
        """

        self._username = username

    @property
    def visible_email(self) -> bool:
        """Gets the visible_email of this SlimUser.


        :return: The visible_email of this SlimUser.
        :rtype: bool
        """
        return self._visible_email

    @visible_email.setter
    def visible_email(self, visible_email: bool):
        """Sets the visible_email of this SlimUser.


        :param visible_email: The visible_email of this SlimUser.
        :type visible_email: bool
        """
        if visible_email is None:
            raise ValueError("Invalid value for `visible_email`, must not be `None`")  # noqa: E501

        self._visible_email = visible_email

    @property
    def website(self) -> str:
        """Gets the website of this SlimUser.


        :return: The website of this SlimUser.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website: str):
        """Sets the website of this SlimUser.


        :param website: The website of this SlimUser.
        :type website: str
        """

        self._website = website