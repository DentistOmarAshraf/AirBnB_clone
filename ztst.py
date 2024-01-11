#!/usr/bin/python3
from models import storage
from models.review import Review

obj = storage.all()
print("")
print("--Reloaded--")
print("")
for k, v in obj.items():
    print(v)
print("")
print("--Review--")
print("")
rev = Review()
rev.place_id = "8787u"
rev.user_id = "999"
rev.text = "hi how are you"
rev.save()
print(rev)
