from flask import Flask, request, jsonify, abort, render_template
import requests
from dotenv import load_dotenv
import os

#Load environment variable from .env file
load_dotenv()

app = Flask(__name__)

#api key 
API_KEY = os.getenv('98402e64a3c3d081d1bbf872f9ad4953')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City not found'}), 404

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        return jsonify({'error': 'City not found'}), 404

    
    data = response.json()
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
    }
    return jsonify(weather)



if __name__ == '__main__':
    app.run(debug=True)