import json
def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    js = 0
    cs = 0
    f = open(file_path)
    ls = json.load(f)
    ls = ls.values()
    for i in ls:
        js += i
        cs += 1
    return js/cs

print(average_expenses("data.json"))
