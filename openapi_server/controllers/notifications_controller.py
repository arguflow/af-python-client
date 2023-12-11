import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.notification_id import NotificationId  # noqa: E501
from openapi_server.models.notification_return import NotificationReturn  # noqa: E501
from openapi_server import util


def get_notifications(page):  # noqa: E501
    """get_notifications

     # noqa: E501

    :param page: Page number of notifications to get
    :type page: int

    :rtype: Union[List[NotificationReturn], Tuple[List[NotificationReturn], int], Tuple[List[NotificationReturn], int, Dict[str, str]]
    """
    return 'do some magic!'


def mark_all_notifications_as_read():  # noqa: E501
    """mark_all_notifications_as_read

     # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def mark_notification_as_read(notification_id):  # noqa: E501
    """mark_notification_as_read

     # noqa: E501

    :param notification_id: JSON request payload with id of notification to mark read
    :type notification_id: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        notification_id = NotificationId.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
