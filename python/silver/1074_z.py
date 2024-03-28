import sys
input = sys.stdin.readline
write = sys.stdout.write

count = 0
def next(r, c, l):
    global count
    l = l//2
    if l == 0:
        return
    box = l*l
    if r<l: # 1, 2사분면
        if c<l: #1사분면
            return next(r, c, l)
        else: # 2사분면
            count += box
            return next(r, c%l, l)
    else:
        if c<l: #3사분면
            count += box*2
            return next(r%l, c, l)
        else: # 4사분면
            count += box*3
            return next(r%l, c%l, l)

# 3, 5, 2
n, r, c = map(int, input().split())
next(r, c, 2**n)
print(count)

'''
def recursive(n, row, col):
    if n == 0:
        return 0
    cur_count = 2 * (row % 2) + (col % 2)
    return 4 * recursive(n-1, row // 2, col // 2) + cur_count
'''