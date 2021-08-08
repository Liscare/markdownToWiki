import json
import requests
import re

import mdLinker
import constant
import cli


def formatter_choice(choice_json):
    """
    Format the choice like Title - Description
    Example for the word "molurus": Python molurus - Species of snake
    :param choice_json: A choice with title and description
    :return: The formatted choice
    """
    return f'{choice_json["title"]} - {choice_json["description"]}'


def fetch(search_query, indicator=False, code=constant.DEFAULT_LANGUAGE, limit=constant.DEFAULT_LIMIT):
    """"
    Fetch one or mo   re Wikipedia page (as a link) from a word or an expression
    See https://wikistats.wmcloud.org/display.php?t=wp for all available language code in Wiki (column named wiki)

        :param limit: Number of response from Wikipedia for each search
        :param search_query: Word or expression to find its matching
        :param indicator: If true, add " [code]" at the end of your word to specify a special language for this one.
        :param code: Language code
        :return: A dict with the word as key and the link as value
    """

    api_url = f'https://api.wikimedia.org/core/v1/wikipedia/{code}/search/page'
    article_url = f'https://{code}.wikipedia.org/wiki/'
    parameters = {'q': search_query, 'limit': limit}
    headers = {'User-Agent': constant.DEFAULT_USER_AGENT}
    response = requests.get(api_url, headers=headers, params=parameters)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        article_url += cli.choice(response_json['pages'], cli.create_question(search_query), formatter_choice)['key']
    name = f'{search_query} [{code.upper()}]' if indicator else search_query
    return {name: article_url}


def fetch_from_md(file_name, lang=constant.DEFAULT_LANGUAGE, limit=constant.DEFAULT_LIMIT):
    """
    Insert Wikipedia link for each markdown link empty (without link).

    Example:
        The string "I live in [France]()." will be replaced by
        "I live in [France](https://en.wikipedia.org/wiki/France).".
    :param limit: Number of response from Wikipedia for each search
    :param lang: Language code
    :param file_name: Name of your markdown file
    :return: Fetched words from Wikipedia as a dictionary (may have duplicate)
    """

    with open(file_name, 'r') as file:
        content = file.read()
    words = re.findall(r'\[(\w+)]\(\)', content)
    words_links = dict()
    for word in words:
        words_links.update(fetch(word, code=lang, limit=limit))
    with open(file_name, 'w') as file_w:
        file_w.write(mdLinker.replace_in_md(content, words_links))
    return words
