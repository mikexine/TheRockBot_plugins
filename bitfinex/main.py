#!/usr/bin/env python

import requests
import json


def BitFinexData():
    url = 'https://api.bitfinex.com/v1/pubticker/btcusd'
    headers = {'User-Agent': '@TheRockBot Telegram Bot', 'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    bid = data['bid']
    ask = data['ask']
    last = data['last_price']
    volume = data['volume']
    high = data['high']
    low = data['low']
    datatext = 'Bitfinex data: \n- last: '+str(last)+' USD\n- volume: '+str(volume)+' BTC\n- bid: '+str(bid)+' USD\n- ask: '+str(ask)+' USD\n- high: '+str(high)+' USD\n- low: '+str(low)+' USD'
    return datatext

def applicable_types():
    return ['text']

def commands():
    return ['bitfinex']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    return BitFinexData()
