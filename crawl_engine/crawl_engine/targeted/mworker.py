from celery import Celery
import requests
import sys
app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')


def rep_google():
    # print("Test")
    GOO_URL = "https://cloudpricingcalculator.appspot.com/static/data/pricelist.json"
    # print("Test2")
    try:
        # print("Test3")
        r = requests.get(GOO_URL, timeout=0.5)
        # print("Test4")
    except Exception as inst:
        print("Failed to fetch data for AWS with %s and %s" % (inst.args, type(inst)))
        sys.exit(1)

    # print("Test5")
    # print("Status code: {}".format(r.status_code))
    # print("Headers: {}".format(r.headers['content-type']))
    # print("Encoding: {}".format(r.encoding))
    data = r.json()
    # print("Test6")
    # print(data["gcp_price_list"].keys())
    return data


def rep_amazon():
    ROOT = "https://pricing.us-east-1.amazonaws.com"
    AWS_URL = "{}/offers/v1.0/aws/index.json".format(ROOT)

    try:
        r = requests.get(AWS_URL)
    except Exception as inst:
        print("Failed to fetch data for AWS with %s and %s" % (inst.args, type(inst)))
        sys.exit(1)
    data = r.json()
    dump = {}
    for offers in data['offers']:
        try:
            nURL = "{}{}".format(ROOT, data['offers'][offers]['currentVersionUrl'])
            # print(nURL)
            rn = requests.get(nURL)
        except Exception as inst:
            print("Failed to load data for {} with {} and {}".format(data['offers'][offers]['offerCode'], inst.args,
                                                                     type(inst)))
            sys.exit(1)
        ndata = rn.json()
        dump[data['offers'][offers]['offerCode']] = ndata
        return ndata


@app.task
def add(x, y):
    return x + y


@app.task
def gfetch():
    return rep_google()


@app.task
def afetch():
    return rep_amazon()