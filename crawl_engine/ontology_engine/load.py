from owlready2 import *


file_path = "file:///Users/Gabriel/Dropbox/Research/Maneuver/OntologyV5/Cloud_WK.owl"

onto = get_ontology(file_path)
onto.load()
print(list(onto.data_properties()))
print(list(onto.object_properties()))
print(list(onto.classes()))
print(onto.name)
# Search Ontology
# print(onto.search(iri="*oregon*"))
# print(onto.Virtual_Machine_Flavor)
# print(onto.search(is_a=onto.OS_Type))
print(onto.search(is_a=onto.OS_Type))
new = onto.Virtual_Machine_Flavor("test")
new.hasOSType = [onto.OS_Type("Linux")]
new.hasStorage = [onto.aStorage("HDD")]
new.inRegion = [onto.Region("Ohio")]
new.hasMemory = [onto.Memory("RAM")]
new.hasCurrency = [onto.Currency("US_Dollar")]
new.hasCPU = [onto.aCPU("CPU")]
new.providedBy = [onto.Provider("Amazon")]

new.hasPrice = [float(0.0058)]
new.hasCPUCount = [1]
new.hasMemoryCount = [float(0.5)]

# print(onto.hasOSType())
print(onto.search(is_a=onto.Virtual_Machine_Flavor))


print(onto.Virtual_Machine_Flavor.hasOSType)
# print(onto.Linux)
# print(onto.subclass_of('Virtual_Machine_Flavor'))
# list(onto.classes())
# print(onto.individuals())


# for indiv in onto.classes():
#     print(indiv)
# print onto.classes()


# onto.save(file = "C.owl", format = "rdfxml")