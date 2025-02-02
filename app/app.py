import os
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    key = os.getenv('API_KEY')
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
    Result = response.json()
    image_url = Result ['url']
    image_title = Result ['title']
    explanation = Result ['explanation']
    return render_template('index.html', landing_image= (image_url), image_title= (image_title), explanation= (explanation))

@app.route('/mars')
def mars():
    return render_template('mars.html')