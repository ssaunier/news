import unittest

from client import News

class NewsTest(unittest.TestCase):
    def test_headlines(self): # Happy Path
        news = News()
        articles = news.headlines("fr")
        self.assertIsInstance(articles, list)
        self.assertTrue(len(articles) > 0)

    def test_search(self):
        news = News()
        articles = news.search("brexit")
        self.assertIsInstance(articles, list)
        self.assertTrue(len(articles) > 0)
