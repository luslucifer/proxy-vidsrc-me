import requests
from flask import Flask, request
from flask_cors import CORS  # Import CORS from flask_cors module
import os 


app = Flask(__name__)
CORS(app)  # Initialize CORS extension with your Flask app

@app.route('/')
def home(): 
    return 'I am alive'

@app.route('/fetch')
def fetch():
    host = request.host
    splitedh =host.split(':')
    port = splitedh[1] 
    url = request.args.get('url')  # Get the 'url' query parameter
    if url:
        res = requests.get(url)
        content = res.content
        text =res.text

        if url.replace(' ','').endswith('.m3u8'):
            splited = text.splitlines()
            for index,line in enumerate(splited): 
                line = line.replace(' ', '')
                if line.startswith('https://'):
                    splited[index]=f'http://172.232.43.70:{port}/fetch?url={line}'
            joined = '\n'.join(splited)
            return joined
        
        return content
    else:
        return port

if __name__ == '__main__':
    app.run()
