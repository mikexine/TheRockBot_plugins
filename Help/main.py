#!/usr/bin/env python

help = """
Available Commands:
 - /price: shows the last BTC/EUR price on TheRock
 - /bitcoin: general Bitcoin data from Blockr API
 - /ticker_[fund]: ticker data from TheRock for a selected fund, replace [fund] with btceur, btcusd, ltcbtc or ltceur. 
 - /bitstamp: ticker data from Bitstamp. 
 - /bitfinex: ticker data from BitFinex. 
 - /btce: ticker data from BTC-e. 
 - /okcoin: ticker data from OkCoin 

Find this bot on github:
- Core: https://github.com/leonjza/hogar
- Plugins at: https://github.com/mikexine/TheRockBot_plugins

 Contact @mikexine for info, bugs, feedback & co.
"""

def applicable_types():
    return ['text']

def commands():
    return ['help', 'start']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):


    return help
