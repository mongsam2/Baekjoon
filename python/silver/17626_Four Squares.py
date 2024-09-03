import math
import bisect

n = int(input())

#counts[i] = 1 + counts[remain]
a = math.floor(n**0.5)
special = set()

for i in range(1, a+1):
    special.add(i*i)

print(special)

