import requests

# API key
api_key = 'faba15617ef54bcba90152316242607'
# Base url
base_url = 'http://api.weatherapi.com/v1' 
#Endpoint to get current weather
endpoint = '/current.json'

url = base_url + endpoint

def get_weather(url):
    '''
    Function to get the weather data from the WeatherAPI.
    Input: URL for the WeatherAPI
    Output: Print the weather data

    Parameters for the WeatherAPI:
    url: URL for the WeatherAPI with the city name and the API key.
    '''
    response = requests.get(url_param)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print("Error:", response.status_code, response.text)

# Get the weather data for the city in loop
while True:
    city = str(input("Enter city: "))
    # Form a URL for the WeatherAPI with the city name and the API key.
    url_param = f"{url}?key={api_key}&q={city}"
    
    #Call the function to get the weather data
    get_weather(url_param)