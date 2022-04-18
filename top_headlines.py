from os import link
from flask import Flask,render_template
import secrets
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html', name = nm)

@app.route('/headlines/<nm>')
def hello_stories(nm):
    api_key = secrets.api_key
    url = f"https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={api_key}"
    res = requests.get(url).json()
    rst, tech_list, i = res['results'], [], 0
    for item in rst:
        if i >= 5: break
        if item['section'] == 'technology':
            tech_list.append(item['title'])
            i += 1
    return render_template('headlines.html', name = nm, stories = tech_list)

@app.route('/links/<nm>')
def hello_links(nm):
    api_key = secrets.api_key
    url = f"https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={api_key}"
    res = requests.get(url).json()
    rst, tech_list, i = res['results'], [], 0
    for item in rst:
        if i >= 5: break
        if item['section'] == 'technology':
            tech_list.append((item['title'], item['url']))
            i += 1
    return render_template('links.html', name = nm, stories = tech_list)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)