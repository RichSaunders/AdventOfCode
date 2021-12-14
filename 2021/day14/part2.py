with open("input.txt") as f:
    input = f.read().splitlines()
    string = input[0]
    rules = {x.split(" -> ")[0]: x.split(" -> ")[1] for x in input[2:]}

pairs = {pair: 0 for pair in rules}
for i in range(len(string) - 1):
    pairs[string[i:i + 2]] += 1

for i in range(40):
    new_pairs = {pair: 0 for pair in rules}
    for pair, count in pairs.items():
        new_pairs[pair[0]+rules[pair]] += pairs[pair]
        new_pairs[rules[pair]+pair[1]] += pairs[pair]

    # pairs = new_pairs

    counts = {}
    for pair, count in pairs.items():
        counts.setdefault(pair[0], 0)
        counts[pair[0]] += count/2
        counts.setdefault(pair[1], 0)
        counts[pair[1]] += count/2

    counts[string[0]] += 0.5
    counts[string[-1]] += 0.5

    print(i, max(counts.values()) - min(counts.values()))
