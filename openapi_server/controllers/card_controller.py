import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.card_metadata import CardMetadata  # noqa: E501
from openapi_server.models.card_metadata_with_file_data import CardMetadataWithFileData  # noqa: E501
from openapi_server.models.create_card_data import CreateCardData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.generate_cards_request import GenerateCardsRequest  # noqa: E501
from openapi_server.models.recommend_cards_request import RecommendCardsRequest  # noqa: E501
from openapi_server.models.return_created_card import ReturnCreatedCard  # noqa: E501
from openapi_server.models.search_card_data import SearchCardData  # noqa: E501
from openapi_server.models.search_card_query_response_body import SearchCardQueryResponseBody  # noqa: E501
from openapi_server.models.suggested_queries_request import SuggestedQueriesRequest  # noqa: E501
from openapi_server.models.suggested_queries_response import SuggestedQueriesResponse  # noqa: E501
from openapi_server.models.update_card_by_tracking_id_data import UpdateCardByTrackingIdData  # noqa: E501
from openapi_server.models.update_card_data import UpdateCardData  # noqa: E501
from openapi_server import util


def create_card(create_card_data):  # noqa: E501
    """create_card

     # noqa: E501

    :param create_card_data: JSON request payload to create a new card (chunk)
    :type create_card_data: dict | bytes

    :rtype: Union[List[ReturnCreatedCard], Tuple[List[ReturnCreatedCard], int], Tuple[List[ReturnCreatedCard], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_card_data = CreateCardData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_suggested_queries_handler(suggested_queries_request):  # noqa: E501
    """create_suggested_queries_handler

     # noqa: E501

    :param suggested_queries_request: JSON request payload to get alternative suggested queries
    :type suggested_queries_request: dict | bytes

    :rtype: Union[List[SuggestedQueriesResponse], Tuple[List[SuggestedQueriesResponse], int], Tuple[List[SuggestedQueriesResponse], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        suggested_queries_request = SuggestedQueriesRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_card(card_id):  # noqa: E501
    """delete_card

     # noqa: E501

    :param card_id: id of the card you want to delete
    :type card_id: str
    :type card_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_card_by_tracking_id(tracking_id):  # noqa: E501
    """delete_card_by_tracking_id

     # noqa: E501

    :param tracking_id: tracking_id of the card you want to delete
    :type tracking_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def generate_off_cards(generate_cards_request):  # noqa: E501
    """generate_off_cards

     # noqa: E501

    :param generate_cards_request: JSON request payload to perform RAG on some cards (chunks)
    :type generate_cards_request: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        generate_cards_request = GenerateCardsRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_card_by_tracking_id(tracking_id):  # noqa: E501
    """get_card_by_tracking_id

     # noqa: E501

    :param tracking_id: tracking_id of the card you want to fetch
    :type tracking_id: str

    :rtype: Union[List[CardMetadata], Tuple[List[CardMetadata], int], Tuple[List[CardMetadata], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recommended_cards(recommend_cards_request):  # noqa: E501
    """get_recommended_cards

     # noqa: E501

    :param recommend_cards_request: JSON request payload to get recommendations of cards similar to the cards in the request
    :type recommend_cards_request: dict | bytes

    :rtype: Union[List[List[CardMetadataWithFileData]], Tuple[List[List[CardMetadataWithFileData]], int], Tuple[List[List[CardMetadataWithFileData]], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        recommend_cards_request = RecommendCardsRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def search_card(page, search_card_data):  # noqa: E501
    """search_card

     # noqa: E501

    :param page: Page number of the search results
    :type page: int
    :param search_card_data: JSON request payload to semantically search for cards (chunks)
    :type search_card_data: dict | bytes

    :rtype: Union[List[SearchCardQueryResponseBody], Tuple[List[SearchCardQueryResponseBody], int], Tuple[List[SearchCardQueryResponseBody], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        search_card_data = SearchCardData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_card(update_card_data):  # noqa: E501
    """update_card

     # noqa: E501

    :param update_card_data: JSON request payload to update a card (chunk)
    :type update_card_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_card_data = UpdateCardData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_card_by_tracking_id(update_card_by_tracking_id_data):  # noqa: E501
    """update_card_by_tracking_id

     # noqa: E501

    :param update_card_by_tracking_id_data: JSON request payload to update a card by tracking_id (chunks)
    :type update_card_by_tracking_id_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_card_by_tracking_id_data = UpdateCardByTrackingIdData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
