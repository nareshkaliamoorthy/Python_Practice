

data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Alicob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

new_list = sorted(data, key=lambda x:(x["age"],x["name"]))
print(new_list)

data.sort(key=lambda x:(x["age"],x["name"]))
print (data)