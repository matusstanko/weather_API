# Get max temperatures for the next days for a city entered by the user. User defines the number of days to forecast. In loop

import requests

# API key
api_key = 'faba15617ef54bcba90152316242607'
# Base url
base_url = 'http://api.weatherapi.com/v1' 
#Endpoint to get current weather
endpoint = '/forecast.json'

url = base_url + endpoint

def get_weather(url):
    '''
    Function to get the weather data from the WeatherAPI.
    Input: URL for the WeatherAPI
    Output: Print the weather data

    Parameters:
    url: URL for the WeatherAPI with the city name and the API key.
    '''
    response = requests.get(url_param)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Get days and max temperature for the city
        date_temp_pairs = [(day['date'], day['day']['maxtemp_c']) for day in data['forecast']['forecastday']]

        print(date_temp_pairs)
    else:
        print("Error:", response.status_code, response.text)

# Get the weather data for the city in loop
while True:
    city = str(input("Enter city: "))
    days = int(input("Enter number of days for forecast: "))
    # Form a URL for the WeatherAPI with the city name and the API key and number of days to forecast
    url_param = f"{url}?key={api_key}&q={city}&days={days}"
    
    #Call the function to get the weather data
    get_weather(url_param)

