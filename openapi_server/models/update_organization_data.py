from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateOrganizationData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, configuration=None, name=None, organization_uuid=None):  # noqa: E501
        """UpdateOrganizationData - a model defined in OpenAPI

        :param configuration: The configuration of this UpdateOrganizationData.  # noqa: E501
        :type configuration: object
        :param name: The name of this UpdateOrganizationData.  # noqa: E501
        :type name: str
        :param organization_uuid: The organization_uuid of this UpdateOrganizationData.  # noqa: E501
        :type organization_uuid: str
        """
        self.openapi_types = {
            'configuration': object,
            'name': str,
            'organization_uuid': str
        }

        self.attribute_map = {
            'configuration': 'configuration',
            'name': 'name',
            'organization_uuid': 'organization_uuid'
        }

        self._configuration = configuration
        self._name = name
        self._organization_uuid = organization_uuid

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateOrganizationData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateOrganizationData of this UpdateOrganizationData.  # noqa: E501
        :rtype: UpdateOrganizationData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def configuration(self) -> object:
        """Gets the configuration of this UpdateOrganizationData.


        :return: The configuration of this UpdateOrganizationData.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration: object):
        """Sets the configuration of this UpdateOrganizationData.


        :param configuration: The configuration of this UpdateOrganizationData.
        :type configuration: object
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def name(self) -> str:
        """Gets the name of this UpdateOrganizationData.


        :return: The name of this UpdateOrganizationData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this UpdateOrganizationData.


        :param name: The name of this UpdateOrganizationData.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_uuid(self) -> str:
        """Gets the organization_uuid of this UpdateOrganizationData.


        :return: The organization_uuid of this UpdateOrganizationData.
        :rtype: str
        """
        return self._organization_uuid

    @organization_uuid.setter
    def organization_uuid(self, organization_uuid: str):
        """Sets the organization_uuid of this UpdateOrganizationData.


        :param organization_uuid: The organization_uuid of this UpdateOrganizationData.
        :type organization_uuid: str
        """
        if organization_uuid is None:
            raise ValueError("Invalid value for `organization_uuid`, must not be `None`")  # noqa: E501

        self._organization_uuid = organization_uuid
