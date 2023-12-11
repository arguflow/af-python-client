import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.collection_data import CollectionData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.file import File  # noqa: E501
from openapi_server.models.set_user_api_key_response import SetUserApiKeyResponse  # noqa: E501
from openapi_server.models.slim_user import SlimUser  # noqa: E501
from openapi_server.models.update_user_data import UpdateUserData  # noqa: E501
from openapi_server.models.user_dto_with_cards import UserDTOWithCards  # noqa: E501
from openapi_server import util


def get_specific_user_card_collections(user_id, page):  # noqa: E501
    """get_specific_user_card_collections

     # noqa: E501

    :param user_id: The id of the user to fetch collections for
    :type user_id: str
    :type user_id: str
    :param page: The page of collections to fetch
    :type page: int

    :rtype: Union[List[CollectionData], Tuple[List[CollectionData], int], Tuple[List[CollectionData], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_files_handler(user_id):  # noqa: E501
    """get_user_files_handler

     # noqa: E501

    :param user_id: The id of the user to fetch files for
    :type user_id: str
    :type user_id: str

    :rtype: Union[List[List[File]], Tuple[List[List[File]], int], Tuple[List[List[File]], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_with_cards_by_id(user_id, page):  # noqa: E501
    """get_user_with_cards_by_id

     # noqa: E501

    :param user_id: The id of the user to fetch
    :type user_id: str
    :type user_id: str
    :param page: The page of cards to fetch
    :type page: int

    :rtype: Union[List[UserDTOWithCards], Tuple[List[UserDTOWithCards], int], Tuple[List[UserDTOWithCards], int, Dict[str, str]]
    """
    return 'do some magic!'


def set_user_api_key():  # noqa: E501
    """set_user_api_key

     # noqa: E501


    :rtype: Union[List[SetUserApiKeyResponse], Tuple[List[SetUserApiKeyResponse], int], Tuple[List[SetUserApiKeyResponse], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_user(update_user_data):  # noqa: E501
    """update_user

     # noqa: E501

    :param update_user_data: JSON request payload to update user information for the auth&#39;ed user
    :type update_user_data: dict | bytes

    :rtype: Union[List[SlimUser], Tuple[List[SlimUser], int], Tuple[List[SlimUser], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_user_data = UpdateUserData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
