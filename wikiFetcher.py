import json
import requests
import re

import mdLinker
import constant


def fetch(search_query, indicator=False, code=constant.DEFAULT_LANGUAGE):
    """"
    Fetch one or mo   re Wikipedia page (as a link) from a word or an expression
    See https://wikistats.wmcloud.org/display.php?t=wp for all available language code in Wiki (column named wiki)

        :param search_query: Word or expression to find its matching
        :param indicator: If true, add " [code]" at the end of your word to specify a special language for this one.
        :param code: Language code
        :return: A dict with the word as key and the link as value
    """

    api_url = f'https://api.wikimedia.org/core/v1/wikipedia/{code}/search/page'
    article_url = f'https://{code}.wikipedia.org/wiki/'
    parameters = {'q': search_query, 'limit': 1}
    headers = {'User-Agent': constant.DEFAULT_USER_AGENT}
    response = requests.get(api_url, headers=headers, params=parameters)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        if len(response_json['pages']) == 1:
            article_url += response_json['pages'][0]['key']
    name = f'{search_query} [{code.upper()}]' if indicator else search_query
    return {name: article_url}


def fetch_from_json(file_name):
    """
    Fetch Wikipedia page from a word or an expression into a JSON file

        :param file_name: File name of a JSON file containing words
        :return: A dict with each word as key with its complete link as value
    """

    with open(file_name) as words:
        words_json = json.load(words)
        result = dict()
        for wikiWord in words_json["wikiwords"]:
            language_options = wikiWord.get('language', {})
            for word in wikiWord["words"]:
                result.update(fetch(word, **language_options))
    return result


def fetch_from_md(file_name, lang=constant.DEFAULT_LANGUAGE):
    """
    Insert Wikipedia link for each markdown link empty (without link).

    Example:
        The string "I live in [France]()." will be replaced by
        "I live in [France](https://en.wikipedia.org/wiki/France).".
    :param lang: Language code
    :param file_name: Name of your markdown file
    :return: None
    """

    with open(file_name, 'r') as file:
        content = file.read()
    words = re.findall(r'\[(\w+)]\(\)', content)
    words_links = dict()
    for word in words:
        words_links.update(fetch(word, code=lang))
    with open(file_name, 'w') as file_w:
        file_w.write(mdLinker.replace_in_md(content, words_links))
