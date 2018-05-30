from horoscope_generator import HoroscopeGenerator

WORDS = {
    'tell_horoscope': {
        'groups': [
            ['tell', 'future'],
            ['say', 'wise'],
            ['how', 'day'],
            ['hows', 'day'],
            ['how', 'today'],
            ['hows', 'today'],
            'horoscope'
        ]
    }
}


def tell_horoscope(text):
    return (HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))
