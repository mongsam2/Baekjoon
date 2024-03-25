n, k = map(int, input().split())

lst = [i for i in range(1, n+1)]
ans = []

idx = k-1
for _ in range(n):
    ans.append(lst.pop(idx))
    if len(lst) == 0:
        break
    idx = (idx+k-1)%len(lst)
ans = map(str, ans)
print("<" + ", ".join(ans) + ">")
            # 1   4   