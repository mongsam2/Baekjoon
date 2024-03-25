import sys
input = sys.stdin.readline

while True:
    lens = list(map(int, input().split()))
    if lens == [0, 0, 0]:
        exit()
    lens.sort()
    if lens[2]**2 == lens[0]**2 + lens[1]**2:
        print("right")
    else:
        print("wrong")