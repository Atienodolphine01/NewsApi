from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    sources = get_news('sources')
    print(sources)
    title = 'Home'
    return render_template('index.html', title=title, sources=sources)


@app.route('/articles/<id>')
def news(id):
    '''
    view news articles page that is detailed
    '''
    title = 'Articles'
    return render_template('articles.html', title=title)
