from unittest.mock import patch
from app import *


@patch('app.requests.get')
def test_get_weather_data(mock_requests):
    mock_response = {
        'main': {
            'temp': 20
        },
        'wind': {
            'speed': 5
        },
        'weather': [
            {
                'description': 'clear sky'
            }
        ]
    }
    mock_requests.return_value.json.return_value = mock_response

    weather_data = get_weather_data(37.7749, -122.4194)

    assert weather_data == {'temperature': 20,
                            'wind_speed': 5, 'weather_description': 'clear sky'}


def test_display_weather_data(capsys):
    weather_data = {'temperature': 15.0,
                    'wind_speed': 5.0, 'weather_description': 'cloudy'}
    display_weather_data(weather_data)
    captured = capsys.readouterr()
    assert 'Temperature: 15.0°C' in captured.out
    assert 'Wind Speed: 5.0 m/s' in captured.out
    assert 'Weather Description: cloudy' in captured.out
