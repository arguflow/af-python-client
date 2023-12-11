import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.slim_user import SlimUser  # noqa: E501
from openapi_server import util


def get_me():  # noqa: E501
    """get_me

     # noqa: E501


    :rtype: Union[List[SlimUser], Tuple[List[SlimUser], int], Tuple[List[SlimUser], int, Dict[str, str]]
    """
    return 'do some magic!'


def login():  # noqa: E501
    """login

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def logout():  # noqa: E501
    """logout

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'
