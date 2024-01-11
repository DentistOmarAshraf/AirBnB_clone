#!/usr/bin/env python3
from models import storage
from models.base_model import BaseModel
from models.user import User

print()
print("--Reloaded Objects--")
print()
all_obj = storage.all()
for k, v in all_obj.items():
    print(v)

print()
print("-- Create a new User --")
print()
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print()
print("-- Create a new User --")
print()
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)
