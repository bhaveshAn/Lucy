import re
import wikipedia


def define_subject(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove('define')
    cleaned_message = ' '.join(words_of_message).rstrip()
    if len(cleaned_message) == 0:
        msg = 'define requires subject words'
        return(msg)

    try:
        wiki_data = wikipedia.summary(cleaned_message, sentences=5)

        regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
        m = regEx.match(wiki_data)
        while m:
            wiki_data = m.group(1) + m.group(2)
            m = regEx.match(wiki_data)

        wiki_data = wiki_data.replace("'", "")
        return(wiki_data)
    except wikipedia.exceptions.DisambiguationError as e:
        return ('Can you please be more specific?')
