import json
import requests
import re

import mdLinker

number_of_results = 1
default_language_code = 'en'  # English
user_agent = "MarkdownToWiki (name@domain.com)"
headers = {
    'User-Agent': user_agent
}
base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'


def fetch(search_query, language_code='en'):
    """"
    Fetch one or more Wikipedia page (as a link) from a word or an expression

        :param language_code: Language code, English by default. (See https://wikistats.wmcloud.org/display.php?t=wp)
        :param search_query: Word or expression to find its matching Wikipedia page
        :return: A dict with the word as key and the link as value
    """

    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)
    article_url = 'https://' + language_code + '.wikipedia.org/wiki/'
    if response.status_code == 200:
        print(response.text)
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
        for wikiWord in words_json["wikiwords"]:
            language_code = wikiWord.get('language_code', default_language_code)
            for word in wikiWord["words"]:
                result.update(fetch(word, language_code))
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
