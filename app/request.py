import json
from tkinter import Image
from turtle import title
from unicodedata import name
from urllib import request, parse
from .models import source, article

Source = source.Source
Article = article.Article

#getting API key
api_key = None
# Getting the movie base url
base_url = None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = f"{base_url}/top-headlines/sources?apiKey={api_key}"

    with request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = process_sources(get_news_response['sources'])

    return news_sources


def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for news_source in sources_list:

        id = news_source['id']
        name = news_source['name']
        url = news_source["url"]
        description = news_source["description"]

        news_source_object = Source(id,name, url,description)
        sources_results.append(news_source_object)

    return sources_results 

def process_articles(articles_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    articles_results = []
    for article in articles_list:

        title = article['title']
        description = article['description']
        url_to_image = article["urlToImage"]
        published_at = article["publishedAt"]
        url = article["url"]
        content = article['content']

        article_object = Article(title, description, url_to_image, published_at, url, content)
        articles_results.append(article_object)

    return articles_results

def select_news_sources(source_name):
    '''
    Function that gets the json response to our url request
    '''
    parsed_params = parse.urlencode(
        {
            'sources': f"{source_name},",
            'apiKey': api_key
        }
    )
    get_news_url = f"{base_url}/everything?{parsed_params}"

    with request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = process_articles(get_news_response['articles'])

    return news_articles