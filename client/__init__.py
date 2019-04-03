import requests

class News:
    BASE_URL = "https://newsapi.org/v2"
    API_KEY = '367f28d82c3b42e2bb224b79b0ef480e'

    def headlines(self, country):
        url = f'{self.BASE_URL}/top-headlines'
        params = {'country': country, 'apiKey': self.API_KEY}
        return self.__get(url, params)

    def search(self, keyword):
        url = f'{self.BASE_URL}/everything'
        params = {'q': keyword, 'apiKey': self.API_KEY}
        return self.__get(url, params)


    def __get(self, url, params):
        response = requests.get(url, params=params)
        json = response.json()
        return [ article['title'] for article in json['articles'] ]

        # articles = []
        # for article in json['articles']:
        #     articles.append(article['title'])
        # return articles
