
#Validate all user IDs are sorted in ascending order
response = {
    "users": [
        {"id": 1, "name": "Alice", "role": "QA"},
        {"id": 4, "name": "Bob", "role": "Dev"},
        {"id": 3, "name": "Charlie", "role": "QA"},
        {"id": 2, "name": "David", "role": "QA"}
    ]
}

try:
    user_list = response["users"]
    sorted_list = sorted(user_list, key=lambda x: x["id"])
    print(sorted_list)
except Exception as e:
    raise ValueError("Error:",e)
