# NewsGPT 

This experiment code is to explore the sentimental analysis of news healines with OpenAI gpt API and News API ([documentation](https://newsapi.org/docs/endpoints/top-headlines)). It would leverage the gpt to inference the news headlines to compute the sentimental rating and correlate the stock sectors. 

## Setup

Dependencies setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Env variables setup
```
touch .env
vim .env
```
In the `.env`, add and file the follows
```
OPENAI_API_KEY=
NEWS_API_KEY=
```

## Usage
with default parameters:
```
python news_sentiment.py
```
with explicit parameters:
```
python news_sentiment.py --category=technology --country=us --keyword=bitcoin
```

The supported `--category`:

- `business` `entertainment` `general` `health` `science` `sports` `technology`

The supported `--country`:

- The [2-letter ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1)

## Output
It would print json result of the correlated stock sector and sentiment rating for the headlines. 
![Screen Shot 2023-04-16 at 5 19 44 PM](https://user-images.githubusercontent.com/31863762/232342835-d8445b3e-e37c-41b7-bd9b-1af12f77499a.png)


## Note
Since the OpenAI testing account is free, it has the rate limiter 3 requests/min. The code would sleep and avoid hitting the cap. Feel free to comment out the line if the testing account is premium.  

## Future Possible Plan
- Experiments with other news api to test accuracy. 
- Need a system to backtest the result.
- Inference the news and correlate individual stocks. 
