# Author: Kelvin Lai <kelvin@firststreet.org>
# Copyright: This module is owned by First Street Foundation


class Api:
    """Creates an Api interface given a response

    Args:
        response (JSON): A JSON response received from the API
    """

    def __init__(self, response):
        if response.get('valid_id') is not None:
            self.valid_id = response.get('valid_id')
        else:
            self.valid_id = True
        self.search_item = response.get('_search_item')