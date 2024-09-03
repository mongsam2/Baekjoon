import sys
from collections import deque
input = sys.stdin.readline

def make_lst(string_lst, n):
    if n == 0:
        return []
    else:
        return string_lst[1:-1].split(",")

def execute(nums, p):
    reverse = 0
    for order in p:
        if order == "R":
            reverse = (reverse+1)%2
        else:
            if len(nums) == 0:
                return False
            elif reverse:
                nums.pop()
            else:
                nums.popleft()
    if reverse:
        nums = nums.reverse()
    return True

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    string_nums = input().rstrip()
    nums_lst = make_lst(string_nums, n)
    nums = deque(nums_lst)
    if execute(nums, p):
        print("[" + ",".join(list(nums)) + "]")
    else:
        print("error")

    