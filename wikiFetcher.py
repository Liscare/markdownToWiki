import json
import requests


class WikiFetcher:
    language_code = 'en'
    search_query = 'solar system'
    number_of_results = 1
    headers = {
        'User-Agent': 'liscare2@protonmail.com'
    }
    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint

    def fetch(self):
        parameters = {'q': self.search_query, 'limit': self.number_of_results}
        response = requests.get(self.url, headers=self.headers, params=parameters)
        if response.status_code == 200:
            response_json = json.loads(response.text)
            for page in response_json['pages']:
                article_url = 'https://' + self.language_code + '.wikipedia.org/wiki/' + page['key']
                print(article_url)
