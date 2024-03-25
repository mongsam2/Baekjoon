# 나이, 가입 순서
import sys
input = sys.stdin.readline
write = sys.stdout.write
n = int(input())
dic = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if age not in dic:
        dic[age] = [name]
    else:
        dic[age].append(name)
lst = sorted(dic.items(), key=lambda x : x[0])
for item in lst:
    age = item[0]
    for name in item[1]:
        write(str(age) + " " + name + "\n")