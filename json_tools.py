import requests
import json

def send_request(requested_url):
    #returns requested data with given url
    return requests.get(requested_url)

def read_json_data(input_data):
    #uses input data and returns it to main program
    return input_data.json()

def not_json(json_data):
    try:
        # print(str(json_data))
        something_json = json.loads(json_data)
    except (ValueError, TypeError) as e:
        # print(f'Your error: {e}')
        return True
    return False

def sanitize_json_data(data_in_json):
    sanitize_data = str(data_in_json).replace("'", '"').replace("True", '"True"').replace("False", '"False').replace("null", '"null"')
    result = json.loads(sanitize_data)
    return result

