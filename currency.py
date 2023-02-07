import json
from nbu import nbu
from mb import mb

with open('mb.json', 'r') as file:
    data = json.load(file)

with open('nbu.json', 'r') as file:
    data1 = json.load(file)

def total_currency():
    nbu()
    mb()
    total = [['DATE', 'CURRENCY', 'NBU', 'MB-buy', 'MB-sale']]
    for currency in data:
        for date in data[currency]:
            tmp = [date, currency, data1[currency][date]["price"], data[currency][date]["buy"], data[currency][date]["sale"]]
            total.append(tmp)
    return total

print(json.dumps(total_currency()))

