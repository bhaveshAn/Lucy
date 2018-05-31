from datetime import datetime


def what_is_time(text):
    return ("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S HOURS'))


def what_is_date(text):
    return ("The date is " + datetime.strftime(datetime.now(), '%m/%d/%Y'))


def what_is_day(text):
    return ("The day is " + datetime.strftime(datetime.now(), '%A'))


def tell_bitcoin_price(text):
    return ("The Current BitCoin Price is 7413.99 US Dollar")
