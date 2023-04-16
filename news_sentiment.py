import json
import sys
from time import sleep

import openai
from decouple import config
from newsapi import NewsApiClient

from news_sources.news_api import get_headlines

openai.api_key = config("OPENAI_API_KEY")
OPENAI_RATE_LIMITER_WINDOW = 20

def parse_arguments():
    arg_dict = {
    "category": 'technology',
    "country": 'us',
    "keyword": None
    }
    
    for i in range(1, len(sys.argv)):
        params = sys.argv[i].split("=")
        key = params[0][2:]
        if key in arg_dict:
            arg_dict[key] = params[1]
    
    return arg_dict

def get_news_sentiment_and_stock_correlation():
    arg_dict = parse_arguments()
    top_headlines_articles = get_headlines(
        category=arg_dict["category"],
        country=arg_dict["country"],
        key_words=arg_dict["keyword"])

    prompt = "You are a helpful assistant. Correlate the text with 11 stock sectors according to the Global Industry Classification Standard and classify the text sentiment and response in positive, neutral or negative.\n"\
        + "Below is the example of input and expected response:\n" \
        + "Input: Moderna/Merck cancer vaccine plus Keytruda delays skin cancer return\n\n" \
        + "Expected Response:\n" \
        + "{\"sector\":{\"value\":\"Health Care\",\"rating\":0.9},\"sentiment\":{\"value\":\"positive\",\"rating\":0.8}}\n" \
        + "make sure the response can be parsed by Python json.loads." \

    for article in top_headlines_articles:
        messages = [{"role": "system", "content": prompt},
                    {"role": "user", "content": article["title"]}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=messages,
            temperature=0.0)
        result = json.loads(response.choices[0].message.content)
        print(result)
        sleep(OPENAI_RATE_LIMITER_WINDOW)

get_news_sentiment_and_stock_correlation()