from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    return render_template('index.html',title=title)

@app.route('/articles/<id>')
def news(id):
    '''
    view news articles page that is detailed
    '''
    title = 'Articles'
    return render_template('articles.html', title= title)