import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    json faylidan jami xarajatlarni oling
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    ls = []
    js = 0
    f = open(file_path)
    f = json.load(f)
    for i in f.values():
        ls.append(i)
        for i in ls:
            js += i
    
    return js

file_path = "data.json"
total = total_expenses(file_path)
print(total)
