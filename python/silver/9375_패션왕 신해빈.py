import sys
input = sys.stdin.readline

def wearing():
    n = int(input())
    cloth_dic = {}
    for _ in range(n):
        name, kind = input().rstrip().split()
        if kind in cloth_dic:
            cloth_dic[kind].append(name)
        else:
            cloth_dic[kind] = ["", name]
    
    ans = 1
    for cloth_lst in cloth_dic.values():
        ans *= len(cloth_lst)
    ans -= 1
    return ans

t = int(input())
for _ in range(t):
    print(wearing())

