import requests

class HttpClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def request(self, method, endpoint, **kwargs):
        url = self.base_url + (endpoint or '')
        response = self.session.request(method, url, **kwargs)
        return response

    def get(self, endpoint=None, params=None):
        url = self.base_url + (endpoint or '')
        response = self.session.get(url, params=params)
        return response
