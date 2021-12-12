with open("input.txt") as f:
    input = f.read().splitlines()
    paths = [x.split("-") for x in input]
    nodes = {}
    for path in paths:
        nodes.setdefault(path[0], []).append(path[1])
        nodes.setdefault(path[1], []).append(path[0])

def duplicateSmall(route):
    pass
    for node in route:
        if node.lower() == node and route.count(node) > 1:
            return True
    return False


def traverse(nodes, route):
    if route[-1] == "end":
        return [route]

    if nodes[route[-1]] == []:
        return []

    paths = []
    for next in nodes[route[-1]]:

        if next.lower() == next:
            if next == "start" or (next in route and duplicateSmall(route)):
                continue

        new_paths = traverse(nodes, route+[next])
        paths += new_paths

    return paths

paths = traverse(nodes, ["start"])
print(len(paths))
