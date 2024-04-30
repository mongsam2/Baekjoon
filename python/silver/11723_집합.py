import sys
input  = sys.stdin.readline
write = sys.stdout.write

sets = [0 for _ in range(21)]

m = int(input())
for _ in range(m):
    comm = input().rstrip().split()
    text = comm[0]
    x = -1
    if text not in ["all", "empty"]:
        x = int(comm[1])
    if text=="add":
        sets[x] = 1
    elif text=="remove":
        sets[x] = 0
    elif text == "check":
        write(str(sets[x])+"\n")
    elif text=="toggle":
        sets[x] = (sets[x]+1)%2
    elif text=="all":
        sets = [1 for _ in range(21)]
    elif text=="empty":
        sets = [0 for _ in range(21)]