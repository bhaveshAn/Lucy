import random

WORDS = {'go_to_sleep': {'groups': ['sleep', 'bye', 'deactivate', 'stop',
         'suspend', 'quit', ['power', 'off'], ['stand', 'down'],
         ['good', 'bye']]}}


def go_to_sleep(text):
    replies = ['See you later!', 'Just call my name and I\'ll be there!']
    return (random.choice(replies))
    quit()
