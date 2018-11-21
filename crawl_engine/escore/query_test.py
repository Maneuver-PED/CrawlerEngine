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

resp = testConnection.recomQuery(test_rec)

print(resp)

for k, v in resp.items():
        print(len(v))

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
