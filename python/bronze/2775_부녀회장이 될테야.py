import sys
input = sys.stdin.readline
write = sys.stdout.write
floor_0 = [i for i in range(15)]
house = [[0 for _ in range(15)] for i in range(14)]
house.insert(0, floor_0)

for floor in range(1, 15):
    for room in range(1, 15):
        house[floor][room] = sum(house[floor-1][:room+1])


t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    write(str(house[k][n]) + "\n")
'''
1 2 3 4 5 6 ... n
sum[]
'''