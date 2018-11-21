import boto.ec2
from boto.ec2.connection import EC2Connection
import pickle
region = boto.ec2.regions()
print(region)

# conn = EC2Connection('AKIAIJ3MW7O4VZMYHE7A', 'iQYps6aUGOOHJ+av/GK4lBrFQCigor5UGxWgU8a5')
# images = conn.get_all_images()
# pickle.dump(images, open("ami_list.p", "wb"))
# print("Done")


print("Loading Data")

l_images = pickle.load(open("ami_list.p", "rb"))
print(len(l_images))
print(l_images.__dict__)
# for i in l_images:
#     print(i)
#     print("{}->{}".format(i.name, i.description))
    # print(i.location)
    # print(i.description)
    # print(i.name)
# print(type(l_images))