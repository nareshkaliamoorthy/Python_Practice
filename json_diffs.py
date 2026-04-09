    #Output: {"name": ("John","Doe")}

def json_difference():
    json1 = {
    "id": 101,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "department": "Engineering",
    "salary": 95000,
    "active": True,
    "address": {
        "street": "123 Main St",
        "city": "San Francisco",
        "zipcode": "94105"
    },
    "skills": ["Python", "JavaScript", "SQL"],
    "projects": [
        {"name": "Project A", "status": "completed"},
        {"name": "Project B", "status": "in-progress"}
    ]
}
    json2 = {
    "id": 101,
    "name": "Alice J.",  # Changed
    "email": "alice.johnson@example.com",  # Changed
    "department": "Engineering",
    "salary": 102000,  # Changed
    "active": True,
    "address": {
        "street": "456 Oak Ave",  # Changed
        "city": "San Francisco",
        "zipcode": "94105"
    },
    "skills": ["Python", "JavaScript", "Go"],  # Changed
    "projects": [
        {"name": "Project A", "status": "completed"},
        {"name": "Project B", "status": "in-progress"}
    ],
    "phone": "555-1234"  # New field
}
    diffs = {}
    for key, value1 in json1.items():
        if key in json2:
            if (value1!=json2.get(key)):
                diffs.update({key:(value1,json2.get(key))})
        else:
            diffs.update({key:value1})
    
    for key, value2 in json2.items():
        if key not in json1:
            diffs.update({key:value2})
            
    print (diffs)

json_difference()