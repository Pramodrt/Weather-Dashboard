import requests
import configparser
from flask import Flask, render_template, request
from requests import api

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
    cityName = request.form['cityName']

    api= get_api_key()
    data = get_Weather_resullts(cityName,api)
    temp = "{0:.2f}".format(data['main']['temp'])
    feels_like = "{0:.2f}".format(data['main']['feels_like'])
    weather = data["weather"][0]['main']
    location = data['name']

    return render_template('results.html',location = location,temp = temp,feels_like = feels_like,weather = weather)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
def get_Weather_resullts(cityName,api_key):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}".format(cityName,'metric',api_key)
    r = requests.get(url)
    return r.json()


if __name__ == "__main__":
    app.run(debug = True)
