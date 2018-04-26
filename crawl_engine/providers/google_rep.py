import requests
import sys


def rep_google():
    print("Test")
    GOO_URL = "https://cloudpricingcalculator.appspot.com/static/data/pricelist.json"
    print("Test2")
    try:
        print("Test3")
        r = requests.get(GOO_URL, timeout=0.5)
        print("Test4")
    except Exception as inst:
        print("Failed to fetch data for AWS with %s and %s" % (inst.args, type(inst)))
        sys.exit(1)

    print("Test5")
    print("Status code: {}".format(r.status_code))
    print("Headers: {}".format(r.headers['content-type']))
    print("Encoding: {}".format(r.encoding))
    data = r.json()
    print("Test6")
    print(data["gcp_price_list"].keys())
    return data