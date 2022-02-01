from email.message import Message
from flask import render_template,redirect, url_for
from . import main
from app.models import article, source
from ..request import get_news_sources, select_news_sources

#views
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    message = "My News App"
    title = 'Home - Welcome to The best Movie Review Website Online'
      # Getting new sources
    news_sources = get_news_sources()
    # upcoming_news = get_news('upcoming')
    upcoming_news = []
    # now_showing_news = get_news('now_playing')
    now_showing_news = []
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, message = message, news_sources = news_sources, upcoming = upcoming_news, now_showing = now_showing_news )

@main.route('/news/<string:source_name>')
def get_articles_per_source(source_name):
    '''
     View movie page function that returns the movie details page and its data
    '''    
    articles = select_news_sources(source_name)
    return render_template('articles.html', articles = articles, source_name = source_name)
