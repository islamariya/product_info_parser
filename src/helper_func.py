"""This module contains "mixin" function"""

import requests

from settings import logging


def get_html(search_url):
    """Opens a search_url and returns a response object"""
    try:
        result = requests.get(search_url)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError) as e:
        print("Connection error!")
        logging.exception(f"Error {e}")
        return False
