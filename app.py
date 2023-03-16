import os
import requests

API_KEY = os.environ.get('OPENWEATHER_API_KEY')


def get_weather_data(latitude, longitude):
    """
    Gets current weather data from OpenWeatherMap API for a given latitude and longitude.
    """
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'

    # Debugging code: print out the URL with the API key
    print(url)

    response = requests.get(url)
    data = response.json()

    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']
    return {'temperature': temperature, 'wind_speed': wind_speed, 'weather_description': weather_description}


def display_weather_data(weather_data):

    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    print(f"Weather Description: {weather_data['weather_description']}")


def main():
    """
    Runs the main loop of the app, prompting the user for latitude and longitude and displaying the current weather data.
    """
    latitude = input("Enter the latitude of your location: ")
    longitude = input("Enter the longitude of your location: ")
    weather_data = get_weather_data(latitude, longitude)
    display_weather_data(weather_data)


if __name__ == '__main__':
    main()
