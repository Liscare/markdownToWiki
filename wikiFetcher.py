import json
import requests


class WikiFetcher:
    language_code = 'en'
    number_of_results = 1
    headers = {
        'User-Agent': 'liscare2@protonmail.com'
    }
    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint

    def fetch(self, search_query):
        parameters = {'q': search_query, 'limit': self.number_of_results}
        response = requests.get(self.url, headers=self.headers, params=parameters)
        article_url = 'https://' + self.language_code + '.wikipedia.org/wiki/'
        if response.status_code == 200:
            response_json = json.loads(response.text)
            if len(response_json['pages']) == 1:
                article_url += response_json['pages'][0]['key']
        return {search_query: article_url}

    def fetch_from_json(self, file_name):
        with open(file_name) as words:
            words_json = json.load(words)
            result = dict()
            for word in words_json["words"]:
                result.update(self.fetch(word))
        return result
