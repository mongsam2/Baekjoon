n = int(input())

def create(cons): # n => 분해합
    s = str(cons)
    ans = cons + sum(map(int, s)) # 문자열 map 가능
    return ans

for cons in range(n+1):
    if create(cons) == n:
        print(cons)
        exit()
print(0)
