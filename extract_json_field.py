

def extract_value():

    json_text = {"data":{"user":{"id":10}}}
    value = json_text.get("data", {}).get("user",{}).get("id")
    print(value)

extract_value()