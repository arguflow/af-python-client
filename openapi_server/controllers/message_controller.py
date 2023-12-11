import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.create_message_data import CreateMessageData  # noqa: E501
from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.edit_message_data import EditMessageData  # noqa: E501
from openapi_server.models.message import Message  # noqa: E501
from openapi_server.models.regenerate_message_data import RegenerateMessageData  # noqa: E501
from openapi_server import util


def create_message_completion_handler(create_message_data):  # noqa: E501
    """create_message_completion_handler

     # noqa: E501

    :param create_message_data: JSON request payload to create a message completion
    :type create_message_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        create_message_data = CreateMessageData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_message_handler(edit_message_data):  # noqa: E501
    """edit_message_handler

     # noqa: E501

    :param edit_message_data: JSON request payload to edit a message and get a new stream
    :type edit_message_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        edit_message_data = EditMessageData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_topic_messages(messages_topic_id):  # noqa: E501
    """get_all_topic_messages

     # noqa: E501

    :param messages_topic_id: The ID of the topic to get messages for
    :type messages_topic_id: str
    :type messages_topic_id: str

    :rtype: Union[List[List[Message]], Tuple[List[List[Message]], int], Tuple[List[List[Message]], int, Dict[str, str]]
    """
    return 'do some magic!'


def regenerate_message_handler(regenerate_message_data):  # noqa: E501
    """regenerate_message_handler

     # noqa: E501

    :param regenerate_message_data: JSON request payload to delete an agent message then regenerate it in a strem
    :type regenerate_message_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        regenerate_message_data = RegenerateMessageData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
