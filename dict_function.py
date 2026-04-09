
user = {"name":"suresh", "age":30, "dept": "qa"}
data = {"name":"suresh", "age":30, "dept": "qa"}
user.update({"team":"ip"})
print(user)
user = {"business":"LS"}
print(user)

print(user.get("age")) #Return None when key is not found

#print(user["age"]) #Throws error when key is not found

print(user | data)
print(user | data)
user.update({"id":1})
print(user)

for key in user.keys():
    print(key)

for value in user.values():
    print(value)


for key,value in user.items():
    print(key, value)

print({**user, **data})