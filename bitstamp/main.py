#!/usr/bin/env python

import requests
import json


def BitstampData():
    url = 'https://www.bitstamp.net/api/ticker/'
    headers = {'User-Agent': '@TheRockBot Telegram Bot', 'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    bid = data['bid']
    ask = data['ask']
    last = data['last']
    volume = data['volume']
    high = data['high']
    low = data['low']
    datatext = 'Bitstamp data: \n- last: '+str(last)+' USD\n- volume: '+str(volume)+' BTC\n- bid: '+str(bid)+' USD\n- ask: '+str(ask)+' USD\n- high: '+str(high)+' USD\n- low: '+str(low)+' USD'
    return datatext

def applicable_types():
    return ['text']

def commands():
    return ['bitstamp']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    return BitstampData()
