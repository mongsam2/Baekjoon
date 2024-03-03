import sys
input = sys.stdin.readline

def order():
    n, m = map(int, input().split()) # 문서의 개수, 출력 순서 확인할 문서의 위치
    docs = list(map(int, input().split())) # 중요도 1이상 9이하 중요도 같을 수 있음
    order_lst = sorted(docs, reverse=True)
    next = order_lst.pop(0) # 나와야 하는 우선도
    idx = 0
    for rank in range(1, n+1): # 나오는 순서
        for _ in range(n):
            doc = docs[idx]
            if next == doc:
                if idx == m:
                    return rank
                next = order_lst.pop(0)
                idx = (idx+1)%n
                break
            idx = (idx+1)%n


t = int(input())

for _ in range(t):
    ans = order()
    print(ans)
