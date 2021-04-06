import json
import requests

language_code = 'en'
search_query = 'solar system'
number_of_results = 1
headers = {
  'User-Agent': 'liscare2@protonmail.com'
}

base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
endpoint = '/search/page'
url = base_url + language_code + endpoint
parameters = {'q': search_query, 'limit': number_of_results}
response = requests.get(url, headers=headers, params=parameters)
if response.status_code == 200:
    responseJson = json.loads(response.text)
    for page in responseJson['pages']:
        article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
        print(article_url)
