#!/usr/bin/env python

import requests
import json


def BtceData():
    url = 'https://btc-e.com/api/3/ticker/btc_usd-btc_eur'
    headers = {'User-Agent': '@TheRockBot Telegram Bot', 'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    bid = data['btc_usd']['sell']
    ask = data['btc_usd']['buy']
    last = data['btc_usd']['last']
    volume = data['btc_usd']['vol_cur']
    high = data['btc_usd']['high']
    low = data['btc_usd']['low']
    datausd = 'BTC-e BTC/USD data: \n- last: '+str(last)+' USD\n- volume: '+str(volume)+' BTC\n- bid: '+str(bid)+' USD\n- ask: '+str(ask)+' USD\n- high: '+str(high)+' USD\n- low: '+str(low)+' USD\n'
    bid = data['btc_eur']['sell']
    ask = data['btc_eur']['buy']
    last = data['btc_eur']['last']
    volume = data['btc_eur']['vol_cur']
    high = data['btc_eur']['high']
    low = data['btc_eur']['low']
    dataeur = '\nBTC-e BTC/EUR data: \n- last: '+str(last)+' EUR\n- volume: '+str(volume)+' EUR\n- bid: '+str(bid)+' EUR\n- ask: '+str(ask)+' EUR\n- high: '+str(high)+' EUR\n- low: '+str(low)+' EUR'
    datatext = datausd + dataeur
    return datatext

def applicable_types():
    return ['text']

def commands():
    return ['btce']

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    return BtceData()
