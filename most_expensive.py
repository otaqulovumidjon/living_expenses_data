import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    ls = []
    js = []
    f = open(file_path)
    f = json.load(f)

    for n in f.keys():
        ls.append(n)

    for i in f.values():
        js.append(i)
        
    x = 0
    y = 0
    while x < len(ls):
        if js[x] > y:
            y = js[x]
        x += 1
    y = js.index(y)
    y = ls[y]
    return y

file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)