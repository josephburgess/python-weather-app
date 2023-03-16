from unittest.mock import patch
from app import get_weather_data


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
