
#{"user_id":1,"user_name":"John"}
def flatten_json():
    user_dict ={"user":{"id":1,"name":"John"}}

    temp_dict = user_dict["user"]
    new_dict = {}

    for key, value in temp_dict.items():
        new_dict["user_"+key] = value

    print(new_dict) 


flatten_json()