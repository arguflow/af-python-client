import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.default_error import DefaultError  # noqa: E501
from openapi_server.models.file_dto import FileDTO  # noqa: E501
from openapi_server.models.update_file_data import UpdateFileData  # noqa: E501
from openapi_server.models.upload_file_data import UploadFileData  # noqa: E501
from openapi_server.models.upload_file_result import UploadFileResult  # noqa: E501
from openapi_server import util


def delete_file_handler(file_id):  # noqa: E501
    """delete_file_handler

     # noqa: E501

    :param file_id: The id of the file to delete
    :type file_id: str
    :type file_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_file_handler(file_id):  # noqa: E501
    """get_file_handler

     # noqa: E501

    :param file_id: The id of the file to fetch
    :type file_id: str
    :type file_id: str

    :rtype: Union[List[FileDTO], Tuple[List[FileDTO], int], Tuple[List[FileDTO], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_image_file(file_name):  # noqa: E501
    """get_image_file

     # noqa: E501

    :param file_name: The name of the image file to return
    :type file_name: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_file_handler(update_file_data):  # noqa: E501
    """update_file_handler

     # noqa: E501

    :param update_file_data: JSON request payload to update a file
    :type update_file_data: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_file_data = UpdateFileData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def upload_file_handler(upload_file_data):  # noqa: E501
    """upload_file_handler

     # noqa: E501

    :param upload_file_data: JSON request payload to upload a file
    :type upload_file_data: dict | bytes

    :rtype: Union[List[UploadFileResult], Tuple[List[UploadFileResult], int], Tuple[List[UploadFileResult], int, Dict[str, str]]
    """
    if connexion.request.is_json:
        upload_file_data = UploadFileData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
