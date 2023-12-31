from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.search_card_data_time_range_inner import SearchCardDataTimeRangeInner
from openapi_server.models.search_card_data_weights_inner import SearchCardDataWeightsInner
from openapi_server import util

from openapi_server.models.search_card_data_time_range_inner import SearchCardDataTimeRangeInner  # noqa: E501
from openapi_server.models.search_card_data_weights_inner import SearchCardDataWeightsInner  # noqa: E501

class SearchCardData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content=None, cross_encoder=None, filters=None, link=None, search_type=None, tag_set=None, time_range=None, weights=None):  # noqa: E501
        """SearchCardData - a model defined in OpenAPI

        :param content: The content of this SearchCardData.  # noqa: E501
        :type content: str
        :param cross_encoder: The cross_encoder of this SearchCardData.  # noqa: E501
        :type cross_encoder: bool
        :param filters: The filters of this SearchCardData.  # noqa: E501
        :type filters: object
        :param link: The link of this SearchCardData.  # noqa: E501
        :type link: List[str]
        :param search_type: The search_type of this SearchCardData.  # noqa: E501
        :type search_type: str
        :param tag_set: The tag_set of this SearchCardData.  # noqa: E501
        :type tag_set: List[str]
        :param time_range: The time_range of this SearchCardData.  # noqa: E501
        :type time_range: List[SearchCardDataTimeRangeInner]
        :param weights: The weights of this SearchCardData.  # noqa: E501
        :type weights: List[SearchCardDataWeightsInner]
        """
        self.openapi_types = {
            'content': str,
            'cross_encoder': bool,
            'filters': object,
            'link': List[str],
            'search_type': str,
            'tag_set': List[str],
            'time_range': List[SearchCardDataTimeRangeInner],
            'weights': List[SearchCardDataWeightsInner]
        }

        self.attribute_map = {
            'content': 'content',
            'cross_encoder': 'cross_encoder',
            'filters': 'filters',
            'link': 'link',
            'search_type': 'search_type',
            'tag_set': 'tag_set',
            'time_range': 'time_range',
            'weights': 'weights'
        }

        self._content = content
        self._cross_encoder = cross_encoder
        self._filters = filters
        self._link = link
        self._search_type = search_type
        self._tag_set = tag_set
        self._time_range = time_range
        self._weights = weights

    @classmethod
    def from_dict(cls, dikt) -> 'SearchCardData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SearchCardData of this SearchCardData.  # noqa: E501
        :rtype: SearchCardData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content(self) -> str:
        """Gets the content of this SearchCardData.


        :return: The content of this SearchCardData.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this SearchCardData.


        :param content: The content of this SearchCardData.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def cross_encoder(self) -> bool:
        """Gets the cross_encoder of this SearchCardData.


        :return: The cross_encoder of this SearchCardData.
        :rtype: bool
        """
        return self._cross_encoder

    @cross_encoder.setter
    def cross_encoder(self, cross_encoder: bool):
        """Sets the cross_encoder of this SearchCardData.


        :param cross_encoder: The cross_encoder of this SearchCardData.
        :type cross_encoder: bool
        """

        self._cross_encoder = cross_encoder

    @property
    def filters(self) -> object:
        """Gets the filters of this SearchCardData.


        :return: The filters of this SearchCardData.
        :rtype: object
        """
        return self._filters

    @filters.setter
    def filters(self, filters: object):
        """Sets the filters of this SearchCardData.


        :param filters: The filters of this SearchCardData.
        :type filters: object
        """

        self._filters = filters

    @property
    def link(self) -> List[str]:
        """Gets the link of this SearchCardData.


        :return: The link of this SearchCardData.
        :rtype: List[str]
        """
        return self._link

    @link.setter
    def link(self, link: List[str]):
        """Sets the link of this SearchCardData.


        :param link: The link of this SearchCardData.
        :type link: List[str]
        """

        self._link = link

    @property
    def search_type(self) -> str:
        """Gets the search_type of this SearchCardData.


        :return: The search_type of this SearchCardData.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type: str):
        """Sets the search_type of this SearchCardData.


        :param search_type: The search_type of this SearchCardData.
        :type search_type: str
        """
        if search_type is None:
            raise ValueError("Invalid value for `search_type`, must not be `None`")  # noqa: E501

        self._search_type = search_type

    @property
    def tag_set(self) -> List[str]:
        """Gets the tag_set of this SearchCardData.


        :return: The tag_set of this SearchCardData.
        :rtype: List[str]
        """
        return self._tag_set

    @tag_set.setter
    def tag_set(self, tag_set: List[str]):
        """Sets the tag_set of this SearchCardData.


        :param tag_set: The tag_set of this SearchCardData.
        :type tag_set: List[str]
        """

        self._tag_set = tag_set

    @property
    def time_range(self) -> List[SearchCardDataTimeRangeInner]:
        """Gets the time_range of this SearchCardData.


        :return: The time_range of this SearchCardData.
        :rtype: List[SearchCardDataTimeRangeInner]
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range: List[SearchCardDataTimeRangeInner]):
        """Sets the time_range of this SearchCardData.


        :param time_range: The time_range of this SearchCardData.
        :type time_range: List[SearchCardDataTimeRangeInner]
        """

        self._time_range = time_range

    @property
    def weights(self) -> List[SearchCardDataWeightsInner]:
        """Gets the weights of this SearchCardData.


        :return: The weights of this SearchCardData.
        :rtype: List[SearchCardDataWeightsInner]
        """
        return self._weights

    @weights.setter
    def weights(self, weights: List[SearchCardDataWeightsInner]):
        """Sets the weights of this SearchCardData.


        :param weights: The weights of this SearchCardData.
        :type weights: List[SearchCardDataWeightsInner]
        """

        self._weights = weights
