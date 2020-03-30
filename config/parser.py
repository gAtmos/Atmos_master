import json, jsonschema # https://json-schema.org/
from sys import stderr

SCHEMA_POSTFIX = ".schema"

def exit_not_found_or_invalid(file_path, exception):
    print(exception, file=stderr)
    print(f"File {file_path} does not exist or is not a valid JSON file.", file=stderr)
    exit(1)

def load(file_path):
    
    try:
        # Open json file
        config = json.load(open(file_path))
    except FileNotFoundError as e:
        exit_not_found_or_invalid(file_path, e)
    
    schema_file_path = file_path[:-5] + SCHEMA_POSTFIX + ".json"

    try:
        jsonschema.validate(config, open(schema_file_path))
    except FileNotFoundError as e:
        exit_not_found_or_invalid(schema_file_path, e)


    return config
    