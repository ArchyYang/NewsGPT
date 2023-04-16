from decouple import config
from newsapi import NewsApiClient

NEWS_API_KEY = config("NEWS_API_KEY")


def get_headlines(category, country, key_words=None):
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(
        category=category,
        country=country,
        q=key_words)
    return top_headlines["articles"]
