import json
import urllib.parse
import urllib.request
from pathlib import Path

BASE_ALPHA_URL = 'https://www.alphavantage.co/query?'


def read_api_key(file_path: str) -> str:
    """
    Given a path to the api key text file, open it and return that api key
    :param file_path: a string path
    :return: api key
    """
    p = Path(file_path)
    with open(p, 'r') as reader:
        for key in reader.readlines():
            return key


def build_url(file_path: str, stock_name: str) -> 'a URL':
    """
    Builds and returns a URL that can be used to ask for stock data
    :param stock_name: name of a specified stock
    :param file_path: a str
    :return: a url
    """
    api_key = read_api_key(file_path)
    parameters = [('function', 'TIME_SERIES_DAILY'), ('symbol', stock_name), ('outputsize', 'full'), ('apikey', api_key)]
    return BASE_ALPHA_URL + urllib.parse.urlencode(parameters)


def get_result(url: str) -> 'a json':
    """
    Takes a URL and returns a python dictionary representing the parsed JSON response
    :param url: url
    :return: dict
    """
    response = None
    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding='utf-8')
        return json.loads(json_text)
    finally:
        if response is not None:
            response.close()
