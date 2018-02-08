import os
import json
import sys

data_dir = '../data/'

data_file = "data_v2.json"
data = json.load(open(data_file))

print("Loaded data from : ", data_file)
# print data

# print (data['config']['regions'])
flat_json = {}

for r in data['config']['regions']:
    flavours = []
    flat_json['region'] = r['region']
    # print r
    print(r['region'])
    # print r['instanceTypes']
    for l in r['instanceTypes']:
        print(l['sizes'])
        for el in l['sizes']:
            renc = {}
            renc['memoryGiB'] = float(el['memoryGiB'])
            renc['vCPU'] = float(el['vCPU'])
            renc['ECU'] = el['ECU']
            renc['cost'] = float(el['valueColumns'][0]['prices']['USD'])
            renc['OS'] = el['valueColumns'][0]['name']
            renc['storageGB'] = el['storageGB']
            renc['flavour'] = el['size']

            print(el)
            flavours.append(renc)
    flat_json[r['region']] = flavours


print (flat_json)
# with open('result.json', 'w') as fp:
#     json.dump(flat_json, fp)

# for k, v in flat_json.iteritems():
#     print k
#     print k['region']




