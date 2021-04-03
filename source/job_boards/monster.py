class Monster:
    def __init__(self, **kwargs):
        url = "https://www.monster.com/jobs/search"
        # ?q=Software+Engineering+Lead&where=City+of+Boston%2C+MA&page=2
        super().__init__(
            url=url,
            **kwargs
        )

    def search_url(self, title, location):
        url = f"{self.url}?q={title}&where={location}&page={page}"
        return url