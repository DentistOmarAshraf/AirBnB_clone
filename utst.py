#!/usr/bin/python3

from models import storage
from models.place import Place

obj = storage.all()
print("")
print("--Reloaded--")
print("")
for k, v in obj.items():
    print(v)
print("")
print("--Create--")
print("")
ne_place = Place()
ne_place.city_id = "2376"
ne_place.user_id = "773"
ne_place.name = "Omar"
ne_place.description = "wide"
ne_place.save()
print(ne_place)
