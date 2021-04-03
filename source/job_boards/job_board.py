class JobBoard:
    def __init__(self, url, location, terms=[]):
        self.url = url

    def search_url(self, page=1):
        url = f"{self.url}?q={title}&where={location}&page={page}"
        return url