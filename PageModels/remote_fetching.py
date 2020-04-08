import requests

class RemoteFetch:
    def __init__(self, link=None):
        self.link = link
        
    def get_content(self):
        content = requests.get(self.link).text
        return content
        