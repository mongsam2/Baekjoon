import sys
input = sys.stdin.readline

n = int(input())
lst = set(map(int, input().split()))
m = int(input())
mlst = list(map(int, input().split()))

for num in mlst:
    if num in lst:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
