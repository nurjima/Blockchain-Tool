import requests
from getAddress import address

balance = []


def search_balance(times):
    times *= 20
    change = address[0+times:20+times]
    add = ','.join(change)
    url = 'https://api.etherscan.io/api?module=account&action=balancemulti&address=' + add + '&tag=latest&apikey=DBB8NBTENXXNKZKAJQKTR8W2UQTNYFF58Y'

    response = requests.get(url)
    bal = response.json()
    inside = bal['result']

    for i in range(20):
        be = inside[i]
        balances = be['balance']
        balance.append(int(balances)/1000000000000000000)


def repeat4times():
    for i in range(5):
        search_balance(i)


repeat4times()
