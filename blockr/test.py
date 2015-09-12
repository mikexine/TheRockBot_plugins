
import requests
import json

def BlockrData():
    url = 'http://btc.blockr.io/api/v1/coin/info'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers = headers)
    data = r.json()
    lb = data['data']['last_block']
    nd = data['data']['next_difficulty']
    nb = 'Current block number: '+str(lb['nb'])
    timeutc = 'Mined: '+str(lb['time_utc'])
    nbtxs = 'Number of txs: '+str(lb['nb_txs'])
    fee = 'Total fees: '+str(lb['fee'])
    diff = 'Difficulty: '+str(round(float(lb['difficulty']),2))
    nextdiff = 'Next difficulty: '+str(round(float(nd['difficulty']),2))
    retarget = 'Retarget in: '+str(nd['retarget_in'])+' blocks'
    retblock = 'Retarget block: '+str(nd['retarget_block'])
    perc = 'Percentage change in difficulty: '+str(round(float(nd['perc']),4))+' %'
    datatext = 'Bitcoin Info from Blockr: \n'+ nb +'\n'+timeutc+'\n'+nbtxs+'\n'+fee+'\n'+diff+'\n'+nextdiff+'\n'+retarget+'\n'+retblock+'\n'+perc
    return datatext

print BlockrData()