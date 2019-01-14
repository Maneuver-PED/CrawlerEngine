import json
from escore.core import ESCore
from escore.pyQueryConstructor import QueryConstructor
import math
import sys

testConnection = ESCore('194.102.63.78')
# newquery = QueryConstructor()
# queryStr = "memory:\"2\" AND vcpu:\"1\""
# queryStr = "memory:*"
# queryBody = newquery.cequery(queryStr)


test_rec = {"0": {"memory": 8000, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 50, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
        "1": {"memory": 8000, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 50, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 20}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Windows"]},
        "2": {"memory": 8000, "cpu": {"type": ["CPU"], "cpu": 8, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 0, "ssd": 0}, "network": {"connections": 60, "dataIn": 60, "dataOut": 60}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Windows"]},
        "3": {"memory": 16000, "cpu": {"type": ["CPU"], "cpu": 8, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 0, "ssd": 0}, "network": {"connections": 60, "dataIn": 60, "dataOut": 60}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}}


sbe = {"1": {"memory": 4096, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 1024, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "2": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 512, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "3": {"memory": 4096, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 512, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "4": {"memory": 512, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 2000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "5": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 500, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"}
}

swc = {"1": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 500, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "2": {"memory": 512, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 1000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "3": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 1000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "4": {"memory": 16000, "cpu": {"type": ["CPU"], "cpu": 8, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 2000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
       "5": {"memory": 256, "cpu": {"type": ["CPU"], "cpu": 1, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 250, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
}

wp = {"1": {"memory": 512, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 1000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
      "2": {"memory": 512, "cpu": {"type": ["CPU"], "cpu": 2, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 2000, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
      "3": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 500, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
      "4": {"memory": 2048, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 500, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"},
      "5": {"memory": 4000, "cpu": {"type": ["CPU"], "cpu": 4, "gpu": 0}, "storage": {"type": ["HDD"], "hdd": 500, "ssd": 0}, "network": {"connections": 20, "dataIn": 20, "dataOut": 2}, "keywords": ["storage application", "big data application"], "operatingSystem": ["Linux"]}, "IP": {"publicIPs": 3, "IPType": "IP4"}

}
resp = testConnection.recomQuery(wp)

print(resp)

for k, v in resp.items():
        print(len(v))

with open('data_wp.json', 'w') as outfile:
    json.dump(resp, outfile)
# lq = newquery.ceQueryString(test_rec)
#
# qresp = {}
# for k, q in lq.items():
#         queryBody = newquery.cequery(q)
#         # print(q)
#         test = testConnection.compQuery(queryBody=queryBody)
#         qresp[k] = test
#
#
# print(qresp)

# import itertools
# cl = [1, 2, 4, 8,  16, 32, 48, 64, 96, 128]
# ml = [1, 2, 4, 8, 16, 32, 64, 128, 256, 384]
# listOLists = [cl, ml]
# nonresp = []
# okresp = []
# newquery = QueryConstructor()
# for list in itertools.product(*listOLists):
#     queryS = "vcpu:{} AND memory:{} AND storage: 0".format(list[0], list[1])
#     queryBody = newquery.cequery(queryS)
#     resp = testConnection._compQuery(queryBody)
#     if len(resp) == 0:
#         nonresp.append(list)
#     else:
#         okresp.append(list)
#
# print(len(nonresp))
# print(len(okresp))
#
# print(okresp)
