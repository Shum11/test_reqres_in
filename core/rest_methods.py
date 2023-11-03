import requests


class RestMethods:
    def __init__(self):
        self.url = "https://reqres.in"

    def get_method(self, req):
        url = self.url + req
        response = requests.get(f"{url}")
        return response

    def post_method(self, req, json):
        url = self.url + req
        response = requests.post(f"{url}", json=json)
        return response

    def put_method(self, req, json):
        url = self.url + req
        response = requests.put(f"{url}", json=json)
        return response

    def patch_method(self, req, json):
        url = self.url + req
        response = requests.patch(f"{url}", json=json)
        return response

    def delete_method(self, req):
        url = self.url + req
        response = requests.delete(f"{url}")
        return response
