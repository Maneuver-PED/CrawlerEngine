import requests
import sys
import json

ROOT = "https://pricing.us-east-1.amazonaws.com"
AWS_URL = "{}/offers/v1.0/aws/index.json".format(ROOT)

try:
    r = requests.get(AWS_URL)
except Exception as inst:
    print("Failed to fetch data for AWS with %s and %s" % (inst.args, type(inst)))
    sys.exit(1)

print("Status code: {}".format(r.status_code))
print("Headers: {}".format(r.headers['content-type']))
print("Encoding: {}".format(r.encoding))
data = r.json()

print("Publication date: {}".format(data['publicationDate']))

print("Offer list: {}".format(data['offers'].keys()))

print("x"*90)
dump = {}
for offers in data['offers']:
    print(data['offers'][offers]['offerCode'])
    print(data['offers'][offers]['currentVersionUrl'])
    print(data['offers'][offers]['versionIndexUrl'])
    # print(data['offers'][offers]['currentRegionIndexUrl'])
    try:
        nURL = "{}{}".format(ROOT, data['offers'][offers]['currentVersionUrl'])
        print(nURL)
        rn = requests.get(nURL)
    except Exception as inst:
        print("Failed to load data for {} with {} and {}".format(data['offers'][offers]['offerCode'], inst.args, type(inst)))
        sys.exit(1)
    print("Status code: {}".format(rn.status_code))
    print("Headers: {}".format(rn.headers['content-type']))
    print("Encoding: {}".format(rn.encoding))
    ndata = rn.json()
    print(ndata)
    print("-" * 90)
    dump[data['offers'][offers]['offerCode']] = ndata


with open('crawled_aws.json', 'w') as fp:
    json.dump(dump, fp)



