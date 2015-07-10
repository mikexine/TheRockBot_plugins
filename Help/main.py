#!/usr/bin/env python

def applicable_types():
    return ['text']

def commands():
    return ['help', 'start']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    # Get the message contents
    return 'Just use the command /price to get the latest price of BTC/EUR on TheRock or /ticker_[insertfund] to get the a ticker (available now: BTCEUR, BTCUSD, LTCBTC, LTCEUR).'
