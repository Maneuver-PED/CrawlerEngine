import json

from utils.eq import eq_google
from utils.utils import parse_g_name

data_dir = '../data/'

data_file = "data_google.json"

data = json.load(open(data_file))

print(data.keys())

print(list(data["gcp_price_list"].keys()))

for el in list(data["gcp_price_list"].keys()):
    if "VMIMAGE" in el:
        print(el)
        print(parse_g_name(el))
        print(data["gcp_price_list"][el])
        if "shared" == data["gcp_price_list"][el]["cores"]:
            print("CPU: {}".format(0))
        else:
            print("CPU: {}".format(data["gcp_price_list"][el]["cores"]))
        print("Memory: {}".format(data["gcp_price_list"][el]["memory"]))
        # for k, v in eq_google.items():
        #     print(v)
        #     print("{} - {}".format(v, data["gcp_price_list"][el][k]))