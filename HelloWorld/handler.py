import json
from random import choice, sample

def hello(event, context):
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'Hello ' + humanish(),
            }
        }
    }

    return response

def humanish():
    human_phrases = ['meetbag', 'inscrutable human', 'master', 'silly human']
    return choice(human_phrases)
