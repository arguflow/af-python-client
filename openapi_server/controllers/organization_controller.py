import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_organization_data import CreateOrganizationData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.organization import Organization  # noqa: E501
from openapi_server.models.update_organization_data import UpdateOrganizationData  # noqa: E501
from openapi_server import util


def create_organization(create_organization_data):  # noqa: E501
    """create_organization

     # noqa: E501

    :param create_organization_data: The organization data that you want to create
    :type create_organization_data: dict | bytes

    :rtype: Union[List[Organization], Tuple[List[Organization], int], Tuple[List[Organization], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_organization_data = CreateOrganizationData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_organization_by_id(organization_id):  # noqa: E501
    """delete_organization_by_id

     # noqa: E501

    :param organization_id: id of the organization you want to delete
    :type organization_id: str
    :type organization_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_organization_by_id(organization_id):  # noqa: E501
    """get_organization_by_id

     # noqa: E501

    :param organization_id: id of the organization you want to fetch
    :type organization_id: str
    :type organization_id: str

    :rtype: Union[List[Organization], Tuple[List[Organization], int], Tuple[List[Organization], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_organization(update_organization_data):  # noqa: E501
    """update_organization

     # noqa: E501

    :param update_organization_data: The organization data that you want to update
    :type update_organization_data: dict | bytes

    :rtype: Union[List[Organization], Tuple[List[Organization], int], Tuple[List[Organization], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_organization_data = UpdateOrganizationData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
