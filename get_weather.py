# Print current weather for a city entered by the user

import requests

# Your API key (replace 'your_api_key' with the actual API key from WeatherAPI)
api_key = 'faba15617ef54bcba90152316242607'

# Base URL for WeatherAPI is http://api.weatherapi.com/v1
# To find the specific endpoint (now its current weather) I need to find specific endpoint.
# The endpoint for current weather is /current.json    (from https://www.weatherapi.com/docs/)

base_url = 'http://api.weatherapi.com/v1/current.json'

# City for which you want to fetch the weather data
city = 'London'

# Complete URL. Here I need to include the API key and the city name in the URL. (for different endpoints I need to include different parameters)
url = f"{base_url}?key={api_key}&q={city}"

# Making the GET request to the WeatherAPI
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extracting relevant data
    current_temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']

    # Print the weather details
    print(f"Current temperature in {city}: {current_temp}°C")
    print(f"Weather condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} kph")
else:
    # Print the error if the request was unsuccessful
    print("Error:", response.status_code, response.text)
