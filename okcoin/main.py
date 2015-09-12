#!/usr/bin/env python

import requests
import json


def OkcoinData():
    url = 'https://www.okcoin.com/api/ticker.do?ok=1'
    headers = {'User-Agent': '@TheRockBot Telegram Bot', 'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    bid = data['ticker']['buy']
    ask = data['ticker']['sell']
    last = data['ticker']['last']
    volume = data['ticker']['vol']
    high = data['ticker']['high']
    low = data['ticker']['low']
    datatext = 'OKCoin data: \n- last: '+str(last)+' USD\n- volume: '+str(volume)+' BTC\n- bid: '+str(bid)+' USD\n- ask: '+str(ask)+' USD\n- high: '+str(high)+' USD\n- low: '+str(low)+' USD'
    return datatext

def applicable_types():
    return ['text']

def commands():
    return ['okcoin']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    return OkcoinData()
