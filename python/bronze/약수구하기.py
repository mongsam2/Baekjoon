'''
n**(1/2)
1 2 5 10
[]     pointer: 0, -1
[1     10] 1, -2
'''
import math
n, k = map(int, input().split())

head = 0
tail = -1
lst = []
mid_number = math.floor(math.sqrt(n)) 
for i in range(1, mid_number+1):
    if n%i == 0:
        lst.insert(head, n//i)
        if n//i != i:
            lst.insert(tail, i)
        head+=1
        tail+=-1
if len(lst) < k:
    print(0)
else:
    print(lst[k-1])