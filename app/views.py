from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/articles/<id>')
def news(id):
    '''
    view news articles page that is detailed
    '''
    return render_template('articles.html')