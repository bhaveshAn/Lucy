from flask import Flask, render_template, request, jsonify
import aiml
import os
import subprocess
from textblob import TextBlob
from nltk.tokenize import word_tokenize

from actions.horoscope import tell_horoscope
from actions.define_subject import define_subject
from actions.news import business_news, agriculture_news, finance_news, foreign_trade_news, infrastructure_news, defence_news, indian_defence_news, political_news, world_news
from actions.ip_address import ip_address
from actions.repeat import repeat_text
from actions.sleep import go_to_sleep
from actions.spelling import spell_text
from actions.tell_joke import tell_joke
from actions.tell_time import what_is_day, what_is_time, what_is_date, tell_bitcoin_price
from actions.system_status import system_status, system_uptime
from actions.general_conversations import who_are_you, toss_coin, how_am_i, who_am_i, where_born, how_are_you, are_you_up, love_you, marry_me, undefined

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText']).lower()
	while True:
	    if message == "quit":
	        exit()
            elif message == "hello":
                bot_response = "Hi"
            elif message == "hi":
                bot_response = "Hello"
	    else:
	        if 'hello' in word_tokenize(message) or 'hi' in word_tokenize(message):
                    bot_response = "Hi"
                elif 'who' in word_tokenize(message) and 'are' in word_tokenize(message) and 'you' in word_tokenize(message):
                    bot_response = who_are_you(message)
                elif 'toss' in word_tokenize(message) and 'coin' in word_tokenize(message):
                    bot_response = toss_coin(message)
                elif 'heads' in word_tokenize(message) and 'tails' in word_tokenize(message):
                    bot_response = toss_coin(message)
                elif 'flip' in word_tokenize(message) and 'coin' in word_tokenize(message):
                    bot_response = toss_coin(message)
                elif 'how' in word_tokenize(message) and 'i' in word_tokenize(message) and 'look' in word_tokenize(message):
                    bot_response = how_am_i(message)
                elif 'how' in word_tokenize(message) and 'am' in word_tokenize(message) and 'i' in word_tokenize(message):
                    bot_response = how_am_i(message)
                elif 'who' in word_tokenize(message) and 'am' in word_tokenize(message) and 'i' in word_tokenize(message):
                    bot_response = who_am_i(message)
                elif 'where' in word_tokenize(message) and 'born' in word_tokenize(message):
                    bot_response = where_born(message)
                elif 'how' in word_tokenize(message) and 'are' in word_tokenize(message) and 'you' in word_tokenize(message):
                    bot_response = how_are_you(message)
                elif 'you' in word_tokenize(message) and 'up' in word_tokenize(message):
                    bot_response = are_you_up(message)
                elif 'love' in word_tokenize(message) and 'you' in word_tokenize(message):
                    bot_response = love_you(message)
                elif 'marry' in word_tokenize(message) and 'me' in word_tokenize(message):
                    bot_response = marry_me(message)
                elif 'business' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = business_news(message)
                elif 'agriculture' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = agriculture_news(message)
                elif 'finance' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = finance_news(message)
                elif 'financial' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = finance_news(message)
                elif 'foreign' in word_tokenize(message) and 'trade' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = foreign_trade_news(message)
                elif 'infrastructure' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = infrastructure_news(message)
                elif 'indian' in word_tokenize(message) and 'defence' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = indian_defence_news(message)
                elif 'international' in word_tokenize(message) and 'defence' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = defence_news(message)
                elif 'political' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = political_news(message)
                elif 'world' in word_tokenize(message) and 'news' in word_tokenize(message):
                    bot_response = world_news(message)
                elif 'tell' in word_tokenize(message) and 'future' in word_tokenize(message):
                    bot_response = tell_horoscope(message)
                elif 'horoscope' in word_tokenize(message):
                    bot_response = tell_horoscope(message)
                elif 'ip' in word_tokenize(message) and 'address' in word_tokenize(message):
                    bot_response = ip_address(message)
                elif 'define' in word_tokenize(message):
                    bot_response = define_subject(message)
                elif 'spell' in word_tokenize(message):
                    bot_response = spell_text(message)
                elif 'repeat' in word_tokenize(message) or 'say' in word_tokenize(message):
                    bot_response = repeat_text(message)
                elif 'how' in word_tokenize(message) and 'systems' in word_tokenize(message):
                    bot_response = system_status(message)
                elif 'how' in word_tokenize(message) and 'system' in word_tokenize(message):
                    bot_response = system_status(message)
                elif 'system' in word_tokenize(message) and 'status' in word_tokenize(message):
                    bot_response = system_status(message)
                elif 'status' in word_tokenize(message):
                    bot_response = system_status(message)
                elif 'uptime' in word_tokenize(message):
                    bot_response = system_uptime(message)
                elif 'time' in word_tokenize(message):
                    bot_response = what_is_time(message)
                elif 'day' in word_tokenize(message):
                    bot_response = what_is_day(message)
                elif 'date' in word_tokenize(message):
                    bot_response = what_is_date(message)
                elif 'bitcoin' in word_tokenize(message) and 'price' in word_tokenize(message):
                    bot_response = tell_bitcoin_price(message)
                elif 'sleep' in word_tokenize(message) or 'bye' in word_tokenize(message):
                    bot_response = go_to_sleep(message)
                elif 'power' in word_tokenize(message) and 'off' in word_tokenize(message):
                    bot_response = go_to_sleep(message)
                elif 'tell' in word_tokenize(message) and 'joke' in word_tokenize(message):
                    bot_response = tell_joke(message)
                else:
                    bot_response = undefined(message)
            subprocess.call(["espeak", "-ven+f3", "-s140", bot_response])
	    return jsonify({'status':'OK','answer':bot_response})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7001))
    app.run(host='0.0.0.0', port=port, debug=True)
