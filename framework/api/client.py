import requests
class APIClient:
    def get(self,url,**kw):
        return requests.get(url,**kw)
    def post(self,url,**kw):
        return requests.post(url,**kw)
