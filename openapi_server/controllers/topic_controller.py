import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_topic_data import CreateTopicData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.delete_topic_data import DeleteTopicData  # noqa: E501
from openapi_server.models.topic import Topic  # noqa: E501
from openapi_server.models.update_topic_data import UpdateTopicData  # noqa: E501
from openapi_server import util


def create_topic(create_topic_data):  # noqa: E501
    """create_topic

     # noqa: E501

    :param create_topic_data: JSON request payload to create chat topic
    :type create_topic_data: dict | bytes

    :rtype: Union[List[Topic], Tuple[List[Topic], int], Tuple[List[Topic], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_topic_data = CreateTopicData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_topic(delete_topic_data):  # noqa: E501
    """delete_topic

     # noqa: E501

    :param delete_topic_data: JSON request payload to delete a chat topic
    :type delete_topic_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        delete_topic_data = DeleteTopicData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_topics():  # noqa: E501
    """get_all_topics

     # noqa: E501


    :rtype: Union[List[List[Topic]], Tuple[List[List[Topic]], int], Tuple[List[List[Topic]], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_topic(update_topic_data):  # noqa: E501
    """update_topic

     # noqa: E501

    :param update_topic_data: JSON request payload to update a chat topic
    :type update_topic_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_topic_data = UpdateTopicData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
