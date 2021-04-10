import json
import requests
import re

import mdLinker

"""
This is a class for finding Wikipedia pages from words/expressions

Attributes:
    language_code (str):
        Language code for search. See https://api.wikimedia.org/wiki/Special:SiteMatrix for all possibilities
        English (en) by default
    email_address (str):
        Your email address for User-Agent in request header
"""
language_code = 'en'
number_of_results = 1
email_address = "name@domain.com"
headers = {
    'User-Agent': email_address
}
base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
url = base_url + language_code + endpoint


def fetch(search_query):
    """"
    Fetch one or more Wikipedia page (as a link) from a word or an expression

        :param search_query: Word or expression to find its matching Wikipedia page
        :return: A dict with the word as key and the link as value
    """

    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)
    article_url = 'https://' + language_code + '.wikipedia.org/wiki/'
    if response.status_code == 200:
        response_json = json.loads(response.text)
        if len(response_json['pages']) == 1:
            article_url += response_json['pages'][0]['key']
    return {search_query: article_url}


def fetch_from_json(file_name):
    """
    Fetch Wikipedia page from a word or an expression into a JSON file

        :param file_name: File name of a JSON file containing words
        :return: A dict with each word as key with its complete link as value
    """

    with open(file_name) as words:
        words_json = json.load(words)
        result = dict()
        for word in words_json["words"]:
            result.update(fetch(word))
    return result


def fetch_from_md(file_name):
    """
    Insert Wikipedia link for each markdown link empty (without link).

    Example:
        The string "I live in [France]()." will be replaced by
        "I live in [France](https://en.wikipedia.org/wiki/France).".
    :param file_name: Name of your markdown file
    :return: None
    """

    with open(file_name, 'r') as file:
        content = file.read()
    words = re.findall(r'\[(.*)]\(\)', content)
    words_links = dict()
    for word in words:
        words_links.update(fetch(word))
    with open(file_name, 'w') as file_w:
        file_w.write(mdLinker.replace_in_md(content, words_links))
