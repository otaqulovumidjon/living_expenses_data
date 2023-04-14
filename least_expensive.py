import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    ks = []
    vs = []

    f = open(file_path)
    f = json.load(f)

    for i in f.keys():
        ks.append(i)
    for n in f.values():
        vs.append(n)
        
    x = 0
    y = 0
    while x < len(vs):
        if vs[x] > y:
            y = vs[x]
        x += 1

        z = 0
        while z < len(vs):
            if vs[z] < y:
                y = vs[z]
                y = vs.index(y)
            z += 1

    return ks[y]

print(least_expensive("data.json"))