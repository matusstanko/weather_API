from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow all origins by default

# Your API key and base URL for WeatherAPI
api_key = 'faba15617ef54bcba90152316242607'
base_url = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city):
    url = f"{base_url}?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
        return weather_info
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_info = get_weather(city)
    if weather_info:
        return jsonify(weather_info), 200
    else:
        return jsonify({'error': 'City not found or API error'}), 404

if __name__ == '__main__':
    app.run(debug=True)
