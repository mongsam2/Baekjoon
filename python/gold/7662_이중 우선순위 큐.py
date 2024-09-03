from collections import deque
import heapq
import os


# dic = 
# 1 3 4 10 11 13
# 13 11 10 4 3 2 1

class DoubleQueue():
    def __init__(self):
        self.dic = {}
        self.max_heap = []
        self.min_heap = []
        self.size = 0
        
    def excute(self, order, num):
        if order == "I":
            self.push(int(num))
        elif order == "D":
            if num == "1":
                self.pop_max()
            elif num == "-1":
                self.pop_min()

    def push(self, x):
        heapq.heappush(self.max_heap, -x)
        heapq.heappush(self.min_heap, x)
        self.size += 1
        if x in self.dic:
           self.dic[x] += 1
        else:
            self.dic[x] = 1

    def pop_max(self):
        if self.size > 0:
            if self.dic[-self.max_heap[0]] > 0:
                self.size -= 1
                self.dic[-self.max_heap[0]] -= 1
                return - heapq.heappop(self.max_heap)
            else:
                heapq.heappop(self.max_heap)
                return self.pop_max()
    
    def pop_min(self):
        if self.size > 0:
            if self.dic[self.min_heap[0]] > 0:
                self.size -= 1
                self.dic[self.min_heap[0]] -= 1
                return heapq.heappop(self.min_heap)
            else:
                heapq.heappop(self.min_heap)
                return self.pop_min()

    def answer(self):
        ans = 0
        if self.size > 0:
            if self.size == 1:
                if self.max_heap:
                    ans = self.pop_max()
                else:
                    ans = self.pop_min()
                print(ans, ans)
            else:
                print(self.pop_max(), self.pop_min())
        else:
            print("EMPTY")
    


import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    q = DoubleQueue()

    for __ in range(k):
        operation, num = input().split()
        q.excute(operation, num)
    
    q.answer()


# 힙에 원소가 하나만 남았을 때, None 출력
'''
1
9
D -1
D -1
I 8088
D 1
I 5585
I 9097
I -6416
D 1
D -1

5585 5585


4
1 3 5 10
1 3 5 10 
10 5 3 2 1

1
9
I 2
I 3
I 5
I 10
D -1
I 1
D 1
D 1
D 1
'''