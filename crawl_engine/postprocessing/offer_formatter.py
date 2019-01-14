import json


def offer_format(data):
    offer_num = 1
    offer_final = []
    for k, v in data.items():
        output_dict = {}
        output_dict["id"] = k
        output_dict["name"] = "offer{}".format(offer_num)
        offer_num += 1
        content = []
        inoffer_num = 1
        for el in v:
            try:
                storageType = el["storageType"]
            except:
                storageType = "HDD"

            try:
                storage = el["storage"]
            except:
                storage = "N/A"

            try:
                os = el["operatingSystem"]
            except:
                os = "N/A"

            try:
                ehnet = el["enhancedNetworkingSupported"]
            except:
                ehnet = "No"

            # if el["pricePerUnit"]["USD"] == '0.0000000000':
            #     break
            try:
                storageType = el["storageType"]
            except:
                storageType = "HDD"
            poffer = {}
            poffer["id"] = inoffer_num
            inoffer_num += 1
            poffer["name"] = el["instanceType"]
            poffer["characteristics"] = {"Compute": {"CPU": el["vcpu"], "GPU": "false", "Memory": el["memory"]},
                                         "Storage": {"StorageType": storageType, "StorageSize": storage},
                                         "Network": {"NetworkPerformance": el["networkPerformance"],
                                                     "EnhancedNetworking": ehnet}, "operatingSystem": os,
                                         "price": el["pricePerUnit"]["USD"]}
            poffer["components"] = ["c1", "c2"]
            # poffer["Storage"] = {"StorageType": storageType, "StorageSize": storage}
            # poffer["Network"] = {"NetworkPerformance": el["networkPerformance"]}
            # poffer["operatingSystem"] = os
            # poffer["price"] = el["pricePerUnit"]["USD"]
            # print(el["networkPerformance"])
            # print(el)
            content.append(poffer)
        output_dict["content"] = content
        offer_final.append(output_dict)
        return offer_final


if __name__ == '__main__':
    swc_file = "/Users/Gabriel/Documents/workspaces/CrawlerEngine2/data/data_swc.json"
    sbe_file = "/Users/Gabriel/Documents/workspaces/CrawlerEngine2/data/data_new.json"
    wp_file = "/Users/Gabriel/Documents/workspaces/CrawlerEngine2/data/data_wp.json"

    with open(wp_file) as f:
        data = json.load(f)

    offer_final = offer_format(data)
    print(offer_final)

    # with open('dp3.json', 'w') as outfile:
    #     json.dump(offer_final, outfile)
