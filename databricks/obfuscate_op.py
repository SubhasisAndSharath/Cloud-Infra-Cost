import json

dict_lookup = {

}

def o(input:str) -> str:
    return input in dict_lookup.keys() and dict_lookup[input] or input

def o2(input_dict:dict) -> str:
    input_str = json.dumps(input_dict)
    for key_dict in dict_lookup.keys():
        if input_str.find(key_dict) >= 0:
            input_str = input_str.replace(key_dict, dict_lookup[key_dict])
    input_dict = json.loads(input_str)
    return input_dict
