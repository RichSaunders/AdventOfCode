import copy

with open("input.txt") as f:
    input = f.read().splitlines()
    paths = [x.split("-") for x in input]
    nodes = {}
    for path in paths:
        nodes.setdefault(path[0], []).append(path[1])
        nodes.setdefault(path[1], []).append(path[0])

def traverse(nodes, location):
    if location == "end":
        return [["end"]]

    if nodes[location] == []:
        return []

    reduced_nodes = copy.deepcopy(nodes)
    if location.lower() == location:
        for destinations in reduced_nodes.values():
            if location in destinations:
                destinations.remove(location)

    paths = []
    for next in nodes[location]:
        new_paths = traverse(copy.deepcopy(reduced_nodes), next)
        for path in new_paths:
            path.append(location)
            paths.append(path)

    return paths

paths = traverse(nodes, "start")
print(len(paths))
