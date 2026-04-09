from jsonschema import validate
import json

def validate_jsonSchema(filepath):
    response_json = {"name":"nareshK", "user_id":123}


    with open (filepath) as file:
       schema_json =  json.load(file)

    validate(response_json,schema_json)

validate_jsonSchema("./schema_template.json")

        

