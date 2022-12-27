import requests
from logging_config import *


def get_status() -> int:
    response = requests.get("http://3ds.altynbank.kz/")
    logger.debug(f"ALTYN - {response.text}")
    logger.debug(f"ALTYN - {response.status_code}")
    return response.status_code
