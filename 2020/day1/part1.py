with open("input.txt", "r") as f:
    input = f.read()

l = input.splitlines()
l = [int(x) for x in l]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == 2020:
            print("%d*%d = %d" % (l[i], l[j], l[i] * l[j]))
            break
