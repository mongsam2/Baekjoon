from heapq import heappop, heappush
import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
heap = []
original_num = {}
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            write("0\n")
        else:
            write(str(heappop(heap)[1])+"\n")
    else:
        heappush(heap, (abs(x), x))