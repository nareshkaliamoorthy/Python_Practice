response = {
    "users": [{"id": 1}, {"id": 2}]
}

user_list = response["users"]
print(user_list)

for data in user_list:
    print(data["id"])