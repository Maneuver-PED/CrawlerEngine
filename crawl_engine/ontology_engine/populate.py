from owlready2 import *
import json
eq_aws = {"us-east-2":	"Ohio",
"us-east-1":	"NVirginia",
"us-west-1":	"Northern_California",
"us-west-2":	"Oregon",
"ap-south-1":	"Mumbai",
"ap-northeast-2":	"Seoul",
"ap-southeast-1": "Singapore",
"ap-southeast-2":	"Sydney",
"ap-northeast-1":	"Tokyo",
"ca-central-1":	"Canada",
"cn-north-1":	"Beijing",
"eu-central-1":	"Frankfurt",
"eu-west-1":	"Ireland",
"eu-west-2":	"London",
"eu-west-3":	"Paris",
"sa-east-1":	"Sao_Paulo"}
file_path = "file:///Users/Gabriel/Dropbox/Research/Maneuver/OntologyV5/Cloud_WK.owl"

onto = get_ontology(file_path)
onto.load()
print("Loading ontology {} ...".format(onto.name))
print("Loading crawled data ...")

data = json.load(open('result.json'))

# print(data.keys())
for k, v in data.items():
    print(k)
    if k in eq_aws:
        # print(v)
        for f in v:
            print(f)
            str_new_inst = "{}_{}_{}".format(f['flavour'].replace(".", ""), eq_aws[k], f['OS'])
            print("Creating new entity {} ...".format(str_new_inst))
            new_inst = onto.Virtual_Machine_Flavor(str_new_inst)

            print("Adding object properties ...")
            new_inst.hasOSType = [onto.OS_Type("Linux")]
            new_inst.hasStorage = [onto.aStorage("HDD")]
            new_inst.inRegion = [onto.Region(eq_aws[k])]
            new_inst.hasMemory = [onto.Memory("RAM")]
            new_inst.hasCurrency = [onto.Currency("US_Dollar")]
            new_inst.hasCPU = [onto.aCPU("CPU")]
            new_inst.providedBy = [onto.Provider("Amazon")]

            print("Adding data properties ...")
            new_inst.hasPrice = [float(f["cost"])]
            new_inst.hasCPUCount = [float(f["vCPU"])]
            new_inst.hasMemoryCount = [float(f["memoryGiB"])]

            print("Entity {} created!".format(str_new_inst))
        # new_entity = onto.Virtual_Machine_Flavor("test")
print(onto.search(is_a=onto.Virtual_Machine_Flavor))

print("Saving ontology ...")
onto.save(file="Test.owl", format="rdfxml")