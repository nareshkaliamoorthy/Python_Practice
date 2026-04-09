
#Validate that there are no duplicate IDs
response = {
    "users": [
        {"id": 1, "name": "Alice", "role": "QA"},
        {"id": 2, "name": "Bob", "role": "Dev"},
        {"id": 3, "name": "Charlie", "role": "QA"},
        {"id": 1, "name": "David", "role": "QA"}
    ]
}
id_list = []
user_role = []
users = response["users"]
for user_data in users:
    id = user_data["id"]
    if id not in id_list:
        id_list.append(id)
    else:
        print("duplicate ID found:", user_data)
    if(user_data["role"] == "QA"):
        user_role.append(user_data)

print(user_role)

#Get all users with role = "QA"



