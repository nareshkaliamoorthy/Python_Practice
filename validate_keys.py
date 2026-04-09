def validate_keys():
    response = {"id":1, "name":"John"}
    expected = ["id","name"]

    
    if (list(response.keys()) == expected):
        print(True)
    else:
        print(False)

validate_keys()