from owlready2 import *

conto = get_ontology("http://maneuver.org/coud_gen.owl")


with conto:
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


print("Classes in ontology: ")
print(list(conto.classes()))