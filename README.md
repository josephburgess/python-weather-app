# Python Weather App

The Weather App is a Python application that uses the OpenWeather API to get the current weather data for a given latitude and longitude. This was a quick practice app for me exploring Python as a new programming language.

## Requirements

To run this app, you will need:

1. Python 3.x
2. An OpenWeather API key

## Installation

  1. Clone this repository to your local machine.
  2. Install the required Python packages: 
  ```bash
  pip install -r requirements.txt
  ```
  3. Set your OpenWeather API key as an environment variable named OPENWEATHER_API_KEY.
  ```bash
  echo "export OPENWEATHER_API_KEY='[INSERTKEYHERE]'" >> .envrc
  ```
  4. Run the app: python app.py.

## Usage

When you run the app, you will be prompted to enter the latitude and longitude of the location you want to get the weather data for. Once you enter the latitude and longitude, the app will make a request to the OpenWeather API and display the current temperature, wind speed, and weather description for that location.

## Testing

To run the test suite, run pytest from the root directory of the project. The test suite includes tests for the get_weather_data() and display_weather_data() functions.