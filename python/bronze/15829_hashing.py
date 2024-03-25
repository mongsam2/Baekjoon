dic = {chr(ord("a")+i):i+1 for i in range(26)}
r = 31
m = 1234567891
def hashing(s, size):
    global r
    global m
    ans = 0
    for i in range(size):
        ans += dic[s[i]]*r**i
    return ans % m

l = int(input())
s = input()

print(hashing(s, l))