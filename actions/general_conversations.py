import random


def who_are_you(text):
    messages = ['I am Lucy , your own personal assistant.',
                'Lucy, didnt I tell you before?',
                'You asked that so many times! I am Lucy']
    return (random.choice(messages))


def toss_coin(text):
    outcomes = ['heads', 'tails']
    return ('I just flipped a coin. It shows ' + random.choice(outcomes))


def how_am_i(text):
    replies = [
        'You are the coolest person, I have ever seen !',
        'My knees go weak when I see you.',
        'You look like the kindest person that I have met.'
    ]
    return (random.choice(replies))


def who_am_i(text):
    return ('You are a brilliant person. I love you!')


def where_born(text):
    return ('I was created by a person named Bhaavesh, in India')


def how_are_you(text):
    return ('I am fine, thank you.')


def are_you_up(text):
    return ('For you , always.')


def love_you(text):
    replies = [
               'I love you too.',
               'You are looking for love in the wrong place.'
              ]
    return (random.choice(replies))


def marry_me(text):
    return ('I have been receiving a lot of marriage proposals recently.')


def undefined(text):
    return ('I dont know what that means!')
