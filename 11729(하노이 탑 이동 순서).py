# input: n(1에 쌓인 원판의 개수)
# lst[n]: hanoi(1~n) 까지 저장
# def hanoi: (int)from_n, (int)to_n, (int)other_n, (int)n
# hanoi(1, 2, 3, n-1) -> hanoi(1, 3, 2, 1) -> hanoi(2, 3, 1, n-1)

n = int(input())
def hanoi(from_n, to_n, other_n, n):
    if n==1:
        print('{} {}'.format(from_n, to_n))
    else:
        hanoi(from_n, other_n, to_n, n-1)
        hanoi(from_n, to_n, other_n, 1)
        hanoi(other_n, to_n, from_n, n-1)
print(2**n-1)
hanoi(1, 3, 2, n)