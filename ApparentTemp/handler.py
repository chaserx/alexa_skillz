import json
import os
import requests


def current_conditions(event, context):
    '''
    NOTE(chaserx): Dark Sky API key stored in AWS System Manger parameter
    store as plain text.
    '''
    darksky_api_key = os.environ.get('DARKSKY_API_KEY')
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': format_response(darksky_request(darksky_api_key)),
            }
        }
    }

    return response

def darksky_request(darksky_api_key):
    '''
    NOTE(chaserx): GPS static to downtown Lexington, KY. The Dark Sky
    request is only for the current conditions.
    '''
    lat = 38.0406
    lon = -84.5037
    url = "https://api.darksky.net/forecast/{}/{},{}?exclude=minutely,hourly,daily,flags".format(darksky_api_key, lat, lon)
    response = requests.get(url)
    return {'status_code': response.status_code, 'full_response': response}

def format_response(response_dict):
    if response_dict['status_code'] == 200:
        response_json = response_dict['full_response'].json()
        temperature = str(response_json['currently']['temperature'])
        apparentTemperature = str(response_json['currently']['apparentTemperature'])
        return 'The current temperature in Lexington is ' + temperature + ' degrees fahrenheit, but it apparently feels like ' + apparentTemperature + ' degrees fahrenheit.'
    else:
        return 'Oh! Something went wrong. I was not able to get data from the Dark Sky weather service.'

