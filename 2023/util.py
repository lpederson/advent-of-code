

def get_input(name: str):
    with open(f"./data/{name}.txt") as inf:
        return inf.readlines()
