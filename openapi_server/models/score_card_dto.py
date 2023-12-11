from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.card_metadata_with_file_data import CardMetadataWithFileData
from openapi_server import util

from openapi_server.models.card_metadata_with_file_data import CardMetadataWithFileData  # noqa: E501

class ScoreCardDTO(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metadata=None, score=None):  # noqa: E501
        """ScoreCardDTO - a model defined in OpenAPI

        :param metadata: The metadata of this ScoreCardDTO.  # noqa: E501
        :type metadata: List[CardMetadataWithFileData]
        :param score: The score of this ScoreCardDTO.  # noqa: E501
        :type score: float
        """
        self.openapi_types = {
            'metadata': List[CardMetadataWithFileData],
            'score': float
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'score': 'score'
        }

        self._metadata = metadata
        self._score = score

    @classmethod
    def from_dict(cls, dikt) -> 'ScoreCardDTO':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScoreCardDTO of this ScoreCardDTO.  # noqa: E501
        :rtype: ScoreCardDTO
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self) -> List[CardMetadataWithFileData]:
        """Gets the metadata of this ScoreCardDTO.


        :return: The metadata of this ScoreCardDTO.
        :rtype: List[CardMetadataWithFileData]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: List[CardMetadataWithFileData]):
        """Sets the metadata of this ScoreCardDTO.


        :param metadata: The metadata of this ScoreCardDTO.
        :type metadata: List[CardMetadataWithFileData]
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def score(self) -> float:
        """Gets the score of this ScoreCardDTO.


        :return: The score of this ScoreCardDTO.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score: float):
        """Sets the score of this ScoreCardDTO.


        :param score: The score of this ScoreCardDTO.
        :type score: float
        """
        if score is None:
            raise ValueError("Invalid value for `score`, must not be `None`")  # noqa: E501

        self._score = score
