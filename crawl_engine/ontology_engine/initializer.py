import json

from owlready2 import *

from utils.eq import eq_aws, eq_OS, eq_google
from utils.utils import parse_a_dtype, parse_g_name


class OntologyEngine:
    def __init__(self, iri="http://maneuver.org/coud_gen.owl"):
        self.iri = iri
        self.conto = None
        self.eq_aws = eq_aws
        self.eq_google = eq_google

    def get_iri(self):
        return self.conto.base_iri

    def generate(self):
        with self.conto:
            class Application(Thing):
                pass

            class Component(Application):
                pass

            class Component_Type(Component):
                pass

            class Operating_System(Component):
                pass

            class Virtual_Machine_Flavor(Component):
                pass

            class Attributes(Thing):
                pass

            class Functional(Attributes):
                pass

            class aCPU(Functional):
                pass

            class aStorage(Functional):
                pass

            class Connection(Functional):
                pass

            class Bandwidth(Connection):
                pass

            class Data(Bandwidth):
                pass

            class Data_In(Data):
                pass

            class Data_Out(Data):
                pass

            class Concurrent(Connection):
                pass

            class IP(Connection):
                pass

            class Latency(Connection):
                pass

            class Memory(Functional):
                pass

            class Uptime(Functional):
                pass

            class NonFunctional(Attributes):
                pass

            class Budget(NonFunctional):
                pass

            class Currency(NonFunctional):
                pass

            class Metric_Units(NonFunctional):
                pass

            class IOPS(Metric_Units):
                pass

            class Max_Size(Metric_Units):
                pass

            class Min_Size(Metric_Units):
                pass

            class OS_Type(NonFunctional):
                pass

            class Linux(OS_Type):
                pass

            class Other(OS_Type):
                pass

            class Windows(OS_Type):
                pass

            class Provider(NonFunctional):
                pass

            class Region(NonFunctional):
                pass

            class Asia_Pacific(Region):
                pass

            class Europe(Region):
                pass

            class North_America(Region):
                pass

            class South_America(Region):
                pass

            class Service_Type(NonFunctional):
                pass

            class Artificial_Intelligence(Service_Type):
                pass

            class Bussiness(Service_Type):
                pass

            class Management(Bussiness):
                pass

            class Workflow(Bussiness):
                pass

            class Compliance_Security(Service_Type):
                pass

            class Dev_Ops(Service_Type):
                pass

            class IDE(Dev_Ops):
                pass

            class Machine_Learning(Service_Type):
                pass

            class Monitoring(Service_Type):
                pass

            class Multimedia_Production(Service_Type):
                pass

            class Persistent_Storage(Service_Type):
                pass

            class Database(Persistent_Storage):
                pass

            class Security(Service_Type):
                pass

            class Back_up(Security):
                pass

            class Certification(Security):
                pass

            class Data_Management(Security):
                pass

            class Data_Destruction(Data_Management):
                pass

            class Data_Transfer(Data_Management):
                pass

            class Encryption(Data_Management):
                pass

            class Migration(Data_Management):
                pass

            class Reporting(Data_Management):
                pass

            class Data_Protection(Security):
                pass

            class Firewall(Data_Protection):
                pass

            class VPN(Data_Protection):
                pass

            class Software(NonFunctional):
                pass

            class Applications(Software):
                pass

            class Application_Support(Applications):
                pass

            # Create object properties

            class contains(ObjectProperty):
                pass

            class has(ObjectProperty):
                pass

            class hasConnection(has):
                range = [Connection]

            class hasCPU(has):
                range = [aCPU]

            class hasCurrency(has):
                range = [Currency]

            class hasMemory(has):
                range = [Memory]

            class hasOSType(has):
                range = [OS_Type]
                domain = [Operating_System]

            class hasService(has):
                range = [Service_Type]

            class hasSoftware(has):
                range = [Software]

            class hasStorage(has):
                range = [aStorage]

            class includes(ObjectProperty):
                pass

            class includesComponent(includes):
                range = [Component_Type]
                domain = [Component]

            class includesServices(includes):
                domain = [Service_Type]
                range = [Dev_Ops, Multimedia_Production, Artificial_Intelligence, Security, Compliance_Security,
                         Monitoring, Persistent_Storage, Bussiness, Machine_Learning]

            class inRegion(ObjectProperty):
                domain = [Region]
                range = [Region]

            class providedBy(ObjectProperty):
                pass

            class provides(ObjectProperty):
                domain = [Provider]
                range = [Application_Support, Monitoring, Uptime]

            class requires(ObjectProperty):
                pass

            # Create data properties

            class CPUCount(DataProperty):
                range = [float]

            class MemoryCount(DataProperty):
                range = [float]

            class Price(DataProperty):
                range = [float]

            class Value(DataProperty):
                domain = [Budget]

            # Add entities
            ecpu = aCPU("CPU")
            egpgpu = aCPU("GPGPU")
            ehdd = aStorage("HDD")
            essd = aStorage("SSD")

            edollar = Currency("US_Dollar")
            eeuro = Currency("Euro")

            esingapore = Asia_Pacific("Singapore")
            emumbai = Asia_Pacific("Mumbai")
            etokyo = Asia_Pacific("Tokyo")
            eseoul = Asia_Pacific("Seoul")
            esidney = Asia_Pacific("Sydney")

            elondon = Europe("London")
            eireland = Europe("Ireland")
            efrankfurt = Europe("Frankfurt")
            eparis = Europe("Paris")

            ecanada = North_America("Canada")
            eohio = North_America("Ohio")
            envirginia = North_America("NVirginia")
            encalifornia = North_America("Northern_California")
            eoregon = North_America("Oregon")
            egov = North_America("GovCloud")

            esaupaulo = South_America("Sao_Paulo")

            eamazon = Provider("Amazon")
            eazure = Provider("Azure")
            egogrid = Provider("GoGrid")
            egoogle = Provider("Google")

            eip = IP("Public_IP")

            erhel = Linux("RHEL")
            elinux = Linux("linux")
            esles = Linux("SLES")
            ewin = Windows("Windows_SQL_Enterpriese")

            ememory = Memory("RAM")

    def get_classes(self):
        return self.conto.classes()

    def get_object_properties(self):
        return self.conto.object_properties()

    def get_data_properties(self):
        return self.conto.data_properties()

    def get_entitites(self):
        return self.conto.individuals()

    def load_ontology(self, generate=True):

        self.conto = get_ontology(self.iri)
        if generate:
            self.generate()
            return 0
        try:
            print("Trying to load ... ")
            self.conto.load()
            print("Loaded")
            return 0
        except Exception as inst:
            print("Failed to  load ontology from {} with {} and {}".format(self.iri, type(inst), inst.args))
            self.generate()
            return 1

    def get_flavours(self):
        return self.conto.search(is_a=self.conto.Virtual_Machine_Flavor)

    def get_regions(self):
        return self.conto.search(is_a=self.conto.Region)

    def reasoner(self):
        with self.conto:
            sync_reasoner()

    def q(self):
        return self.conto.search(hasCPUCount=1.0, hasMemoryCount=2.0)

    def sync(self, data, provider):
        if provider == 'amazon':
            print("Staring amazon entity syncronization ... ")
            try:
                for k, v in data.items():
                    if k in self.eq_aws:
                        for f in v:
                            print(f)
                            str_new_inst = "{}_{}_{}".format(f['flavour'].replace(".", ""), self.eq_aws[k], f['OS'])
                            print("Creating new entity {} ...".format(str_new_inst))
                            new_inst = self.conto.Virtual_Machine_Flavor(str_new_inst)

                            print("Adding object properties ...")
                            new_inst.hasOSType = [self.conto.OS_Type(eq_OS[f['OS']])]
                            # new_inst.hasStorage = [self.conto.aStorage("HDD")]
                            new_inst.hasStorage = [self.conto.aStorage(parse_a_dtype(f['storageGB']))]
                            new_inst.inRegion = [self.conto.Region(self.eq_aws[k])]
                            new_inst.hasMemory = [self.conto.Memory("RAM")]
                            new_inst.hasCurrency = [self.conto.Currency("US_Dollar")]
                            new_inst.hasCPU = [self.conto.aCPU("CPU")]
                            new_inst.providedBy = [self.conto.Provider("Amazon")]

                            print("Adding data properties ...")
                            new_inst.hasPrice = [float(f["cost"])]
                            new_inst.hasCPUCount = [float(f["vCPU"])]
                            new_inst.hasMemoryCount = [float(f["memoryGiB"])]

                            print("Entity {} created!".format(str_new_inst))
                            # new_entity = onto.Virtual_Machine_Flavor("test")
            except Exception as inst:
                print("Failed to syncronize amazon entities with {} and {}".format(type(inst), inst.args))
                sys.exit(1)
            print("Syncronization complete. ")
        if provider == 'google':
            print("Staring google entity syncronization ... ")
            for el in list(data["gcp_price_list"].keys()):
                if "VMIMAGE" in el:
                    for k, v in self.eq_google.items():
                        print(el)
                        str_new_inst = "{}_{}_{}".format(parse_g_name(el), v, "linux")
                        print("Creating new entity {} ...".format(str_new_inst))
                        new_inst = self.conto.Virtual_Machine_Flavor(str_new_inst)

                        print("Adding object properties ...")
                        new_inst.hasOSType = [self.conto.OS_Type("Linux")]   # todo: modify to add more than linux
                        new_inst.hasStorage = [self.conto.aStorage("HDD")]   # todo: modify to add ssd as well as hdd
                        new_inst.inRegion = [self.conto.Region(v)]
                        new_inst.hasMemory = [self.conto.Memory("RAM")]
                        new_inst.hasCurrency = [self.conto.Currency("US_Dollar")]
                        new_inst.hasCPU = [self.conto.aCPU("CPU")]
                        new_inst.providedBy = [self.conto.Provider("Google")]

                        print("Adding data properties ...")
                        new_inst.hasPrice = [float(data["gcp_price_list"][el][k])]
                        if "shared" == data["gcp_price_list"][el]["cores"]:
                            new_inst.hasCPUCount = [float(0)]
                        else:
                            new_inst.hasCPUCount = [float(data["gcp_price_list"][el]["cores"])]
                        new_inst.hasMemoryCount = [float(data["gcp_price_list"][el]["memory"])]

                        print("Entity {} created!".format(str_new_inst))

    def dump(self):
        self.conto.save(file="Generated_2.owl", format="rdfxml")


print("Staring ontology engine")
test = OntologyEngine()

print(test.load_ontology())
print(test.get_iri())

print("Classes in ontology: ")
print(list(test.get_classes()))

print("Object Properties: ")
print(list(test.get_object_properties()))

print("Data Properties: ")
print(list(test.get_data_properties()))

print("Sync ontology with new crawled data")
data = json.load(open('result.json'))
test.sync(data, 'amazon')

data2 = json.load(open('data_google.json'))
test.sync(data2, 'google')

print("Entities: ")
print(list(test.get_entitites()))

print("Flavours: ")
print(list(test.get_flavours()))
print("Total Entitites {}".format(len(list(test.get_flavours()))))

print("Regions: ")     #  todo: check duplicate region generation
print(list(test.get_regions()))


# test.reasoner()
print(test.q())
print(len(list(test.q())))
test.dump()
