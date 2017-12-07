import os
import json
import sys

data_dir = '../data/'

data_file = "data_v2.json"
data = json.load(open(data_file))

print "Loaded data from : ", data_file
# print data

# print data['config']['regions']

flattened = []
for r in data['config']['regions']:
    flattene_data = {}
    print "Region: {}".format(r['region'])
    flattened.append(flattene_data)
    flattene_data['region'] = r['region']
    instance_types = []
    for t in r['instanceTypes']:
        instance_type = {}
        print "#####" * 100
        print "Type: {}".format(t['type'])
        instance_type['type'] = t['type']
        list_meta = []
        for f in t['sizes']:
            meta = {}
            print "-----" * 100
            print "Flavor: {}".format(f['size'])
            meta['flavour'] = f['size']
            print "Memory: {}".format(f['memoryGiB'])
            meta['memory'] = f['memoryGiB']
            print "vCPU: {}".format(f['vCPU'])
            meta['vCPU'] = f['vCPU']
            print "ECU: {}".format(f['ECU'])
            meta['ECU'] = f['ECU']
            print "OS: {}".format(f['valueColumns'][0]['name'])
            meta['OS'] = f['valueColumns'][0]['name']
            print "Price: {}".format(f['valueColumns'][0]['prices'])
            meta['price'] = f['valueColumns'][0]['prices']
            print "Storage: {}".format(f['storageGB'])
            meta['storageGB'] = f['storageGB']
            list_meta.append(meta)
        # instance_type['meta'] = list_meta
        flattene_data['meta'] = list_meta
        flattened.append(flattene_data)


    # print "Flavores: {}".format(r['instanceTypes'])
print flattened

