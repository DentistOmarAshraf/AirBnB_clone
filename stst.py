#!/usr/bin/python3

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

obj = storage.all()
print("")
print("--Reloaded--")
print("")
for k, v in obj.items():
    print(v)

print("")
print("--new state--")
print("")
my_st = State()
my_st.name = "Cairo"
my_st.save()
print(my_st)

print("")
print(" --new city--")
print("")
my_cit = City()
my_cit.state_id = "8873"
my_cit.name = "Egypt"
my_cit.save()
print(my_cit)

print("")
print(" --new amenity-- ")
print("")
my_am = Amenity()
my_am.name = "I don't know what is amenity"
my_am.save()
print(my_am)
