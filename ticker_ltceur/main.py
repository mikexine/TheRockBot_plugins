#!/usr/bin/env python

import requests
import json


fund  = 'ltceur'

def TheRockData(fund):
    url = 'https://www.therocktrading.com/api/ticker/'+fund.upper()
    headers = {'User-Agent': '@TheRockBot Telegram Bot', 'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    bid = data['result'][0]['bid']
    ask = data['result'][0]['ask']
    last = data['result'][0]['last']
    volume = data['result'][0]['volume_traded']
    datatext = fund+' data: \n- last: '+str(last)+' EUR\n- volume: '+str(volume)+' LTC\n- bid: '+str(bid)+' EUR\n- ask: '+str(ask)+' EUR'
    return datatext

def applicable_types():
    return ['text']

def commands():
    return ['ticker_'+fund, 'ticker'+fund]

def should_reply():
    return True

def reply_type():
    return 'text'

def run(message):
    return TheRockData(fund)