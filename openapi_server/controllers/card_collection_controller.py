import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.add_card_to_collection_data import AddCardToCollectionData  # noqa: E501
from openapi_server.models.bookmark_data import BookmarkData  # noqa: E501
from openapi_server.models.card_collection import CardCollection  # noqa: E501
from openapi_server.models.collection_data import CollectionData  # noqa: E501
from openapi_server.models.create_card_collection_data import CreateCardCollectionData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.delete_collection_data import DeleteCollectionData  # noqa: E501
from openapi_server.models.remove_bookmark_data import RemoveBookmarkData  # noqa: E501
from openapi_server.models.update_card_collection_data import UpdateCardCollectionData  # noqa: E501
from openapi_server import util


def add_bookmark(page_or_card_collection_id, add_card_to_collection_data):  # noqa: E501
    """add_bookmark

     # noqa: E501

    :param page_or_card_collection_id: The id of the collection to add the card to
    :type page_or_card_collection_id: str
    :type page_or_card_collection_id: str
    :param add_card_to_collection_data: JSON request payload to add a card to a collection (bookmark it)
    :type add_card_to_collection_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        add_card_to_collection_data = AddCardToCollectionData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_card_collection(create_card_collection_data):  # noqa: E501
    """create_card_collection

     # noqa: E501

    :param create_card_collection_data: JSON request payload to cretea a CardCollection
    :type create_card_collection_data: dict | bytes

    :rtype: Union[List[CardCollection], Tuple[List[CardCollection], int], Tuple[List[CardCollection], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_card_collection_data = CreateCardCollectionData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_bookmark(page_or_card_collection_id, remove_bookmark_data):  # noqa: E501
    """delete_bookmark

     # noqa: E501

    :param page_or_card_collection_id: The id of the collection to remove the bookmark&#39;ed card from
    :type page_or_card_collection_id: str
    :type page_or_card_collection_id: str
    :param remove_bookmark_data: JSON request payload to remove a card to a collection (un-bookmark it)
    :type remove_bookmark_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        remove_bookmark_data = RemoveBookmarkData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_card_collection(delete_collection_data):  # noqa: E501
    """delete_card_collection

     # noqa: E501

    :param delete_collection_data: JSON request payload to delete a CardCollection
    :type delete_collection_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        delete_collection_data = DeleteCollectionData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_bookmarks(collection_id, page):  # noqa: E501
    """get_all_bookmarks

     # noqa: E501

    :param collection_id: The id of the collection to get the cards from
    :type collection_id: str
    :type collection_id: str
    :param page: The page of cards to get from the collection
    :type page: int

    :rtype: Union[List[BookmarkData], Tuple[List[BookmarkData], int], Tuple[List[BookmarkData], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_logged_in_user_card_collections(page_or_card_collection_id):  # noqa: E501
    """get_logged_in_user_card_collections

     # noqa: E501

    :param page_or_card_collection_id: The page of collections to fetch
    :type page_or_card_collection_id: int

    :rtype: Union[List[CollectionData], Tuple[List[CollectionData], int], Tuple[List[CollectionData], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_card_collection(update_card_collection_data):  # noqa: E501
    """update_card_collection

     # noqa: E501

    :param update_card_collection_data: JSON request payload to update a CardCollection
    :type update_card_collection_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_card_collection_data = UpdateCardCollectionData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
