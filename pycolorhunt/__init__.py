import ast
import re

import requests


class ColorHuntException(Exception):
    pass


class ColorHunt:
    BASE_URL = 'http://colorhunt.co/hunt.php'
    ENDPOINTS = ['hot', 'popular', 'random']

    def __init__(self, sort_key='popular', page=1):
        self.sort_key = sort_key
        self.page = page

    def _get(self, page, sort_key):
        data = {
            'step': page,
            'sort': sort_key,
            'names': ''
        }
        r = requests.post(self.BASE_URL, data=data)
        try:
            data_str = re.match(r'<script>arr\s*=\s*(\[.*\])', r.text).groups()[0]
        except IndexError:
            raise ColorHuntException('Unable to fetch data from Color hunt.')
        return ast.literal_eval(data_str)

    def _parse(self, data):
        for entry in data:
            entry['code'] = re.findall(r'.{6}', entry['code'])
        return data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            data = self._get(self.page, self.sort_key)
            if not data:
                raise StopIteration
            self.page += 1
            return self._parse(data)
        except SyntaxError:
            raise StopIteration
        except ColorHuntException:
            raise
