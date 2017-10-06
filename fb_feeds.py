from json import loads
from urllib import request

ACCESS_TOKEN = 'FILL_ME'  # https://developers.facebook.com/docs/graph-api
BASE_URL = 'https://graph.facebook.com/v2.10/'


def get_stories():
    url = BASE_URL + '/me/feed?access_token=' + ACCESS_TOKEN
    has_next = True
    while has_next:
        data = loads(request.urlopen(url).read())
        for item in data['data']:
            story = item.get('story', {})
            if story:
                print(item['created_time'], story)

        has_next = 'next' in data.get('paging', {})
        if has_next:
            url = data['paging']['next']
        else:
            has_next = False


def get_messages():
    url = BASE_URL + '/me/feed?access_token=' + ACCESS_TOKEN
    has_next = True
    while has_next:
        data = loads(request.urlopen(url).read())
        for item in data['data']:
            message = item.get('message', {})
            if message:
                print(item['created_time'], message)

        has_next = 'next' in data.get('paging', {})
        if has_next:
            url = data['paging']['next']
        else:
            has_next = False
