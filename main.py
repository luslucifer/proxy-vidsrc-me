import requests
from flask import Flask, request
import os 

app = Flask(__name__)

@app.route('/')
def home(): 
    return 'I am alive'

@app.route('/fetch')
def fetch():
    url = request.args.get('url')  # Get the 'url' query parameter
    if url:
        # You can use requests.get() here to fetch the content of the provided URL
        res = requests.get(url).content
        return res
    else:
        return 'No URL provided'

if __name__ == '__main__':
    app.run()
