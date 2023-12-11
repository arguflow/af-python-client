from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateCardByTrackingIdData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, card_html=None, card_uuid=None, link=None, metadata=None, private=None, time_stamp=None, tracking_id=None):  # noqa: E501
        """UpdateCardByTrackingIdData - a model defined in OpenAPI

        :param card_html: The card_html of this UpdateCardByTrackingIdData.  # noqa: E501
        :type card_html: str
        :param card_uuid: The card_uuid of this UpdateCardByTrackingIdData.  # noqa: E501
        :type card_uuid: str
        :param link: The link of this UpdateCardByTrackingIdData.  # noqa: E501
        :type link: str
        :param metadata: The metadata of this UpdateCardByTrackingIdData.  # noqa: E501
        :type metadata: object
        :param private: The private of this UpdateCardByTrackingIdData.  # noqa: E501
        :type private: bool
        :param time_stamp: The time_stamp of this UpdateCardByTrackingIdData.  # noqa: E501
        :type time_stamp: str
        :param tracking_id: The tracking_id of this UpdateCardByTrackingIdData.  # noqa: E501
        :type tracking_id: str
        """
        self.openapi_types = {
            'card_html': str,
            'card_uuid': str,
            'link': str,
            'metadata': object,
            'private': bool,
            'time_stamp': str,
            'tracking_id': str
        }

        self.attribute_map = {
            'card_html': 'card_html',
            'card_uuid': 'card_uuid',
            'link': 'link',
            'metadata': 'metadata',
            'private': 'private',
            'time_stamp': 'time_stamp',
            'tracking_id': 'tracking_id'
        }

        self._card_html = card_html
        self._card_uuid = card_uuid
        self._link = link
        self._metadata = metadata
        self._private = private
        self._time_stamp = time_stamp
        self._tracking_id = tracking_id

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateCardByTrackingIdData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateCardByTrackingIdData of this UpdateCardByTrackingIdData.  # noqa: E501
        :rtype: UpdateCardByTrackingIdData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_html(self) -> str:
        """Gets the card_html of this UpdateCardByTrackingIdData.


        :return: The card_html of this UpdateCardByTrackingIdData.
        :rtype: str
        """
        return self._card_html

    @card_html.setter
    def card_html(self, card_html: str):
        """Sets the card_html of this UpdateCardByTrackingIdData.


        :param card_html: The card_html of this UpdateCardByTrackingIdData.
        :type card_html: str
        """

        self._card_html = card_html

    @property
    def card_uuid(self) -> str:
        """Gets the card_uuid of this UpdateCardByTrackingIdData.


        :return: The card_uuid of this UpdateCardByTrackingIdData.
        :rtype: str
        """
        return self._card_uuid

    @card_uuid.setter
    def card_uuid(self, card_uuid: str):
        """Sets the card_uuid of this UpdateCardByTrackingIdData.


        :param card_uuid: The card_uuid of this UpdateCardByTrackingIdData.
        :type card_uuid: str
        """

        self._card_uuid = card_uuid

    @property
    def link(self) -> str:
        """Gets the link of this UpdateCardByTrackingIdData.


        :return: The link of this UpdateCardByTrackingIdData.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link: str):
        """Sets the link of this UpdateCardByTrackingIdData.


        :param link: The link of this UpdateCardByTrackingIdData.
        :type link: str
        """

        self._link = link

    @property
    def metadata(self) -> object:
        """Gets the metadata of this UpdateCardByTrackingIdData.


        :return: The metadata of this UpdateCardByTrackingIdData.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this UpdateCardByTrackingIdData.


        :param metadata: The metadata of this UpdateCardByTrackingIdData.
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def private(self) -> bool:
        """Gets the private of this UpdateCardByTrackingIdData.


        :return: The private of this UpdateCardByTrackingIdData.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private: bool):
        """Sets the private of this UpdateCardByTrackingIdData.


        :param private: The private of this UpdateCardByTrackingIdData.
        :type private: bool
        """

        self._private = private

    @property
    def time_stamp(self) -> str:
        """Gets the time_stamp of this UpdateCardByTrackingIdData.


        :return: The time_stamp of this UpdateCardByTrackingIdData.
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp: str):
        """Sets the time_stamp of this UpdateCardByTrackingIdData.


        :param time_stamp: The time_stamp of this UpdateCardByTrackingIdData.
        :type time_stamp: str
        """

        self._time_stamp = time_stamp

    @property
    def tracking_id(self) -> str:
        """Gets the tracking_id of this UpdateCardByTrackingIdData.


        :return: The tracking_id of this UpdateCardByTrackingIdData.
        :rtype: str
        """
        return self._tracking_id

    @tracking_id.setter
    def tracking_id(self, tracking_id: str):
        """Sets the tracking_id of this UpdateCardByTrackingIdData.


        :param tracking_id: The tracking_id of this UpdateCardByTrackingIdData.
        :type tracking_id: str
        """
        if tracking_id is None:
            raise ValueError("Invalid value for `tracking_id`, must not be `None`")  # noqa: E501

        self._tracking_id = tracking_id
