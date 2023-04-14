import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    f = open(file_path)
    f = json.load(f)
    return f

print(get_data("data.json"))