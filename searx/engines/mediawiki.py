from json import loads
from urllib import urlencode, quote

url = 'https://en.wikipedia.org/'

search_url = url + 'w/api.php?action=query&list=search&{query}&srprop=timestamp&format=json&sroffset={offset}'  # noqa

number_of_results = 10


def request(query, params):
    offset = (params['pageno'] - 1) * 10
    params['url'] = search_url.format(query=urlencode({'srsearch': query}),
                                      offset=offset)
    return params


def response(resp):
    search_results = loads(resp.text)
    res = search_results.get('query', {}).get('search', [])
    return [{'url': url + 'wiki/' + quote(result['title'].replace(' ', '_').encode('utf-8')),  # noqa
        'title': result['title']} for result in res[:int(number_of_results)]]
