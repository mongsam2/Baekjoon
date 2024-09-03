import sys
import heapq

input = sys.stdin.readline
write = sys.stdout.write
min_heap = []

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(min_heap) == 0:
            write("0\n")
        else:
            write(str(-heapq.heappop(min_heap))+"\n")
    else:
        heapq.heappush(min_heap, -x)