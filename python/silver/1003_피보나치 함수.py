import sys
input = sys.stdin.readline
write = sys.stdout.write

fib = [0 for _ in range(41)]
count = [[0, 0] for _ in range(41)]
fib[0] = 0
fib[1] = 1
count[0] = [1, 0]
count[1] = [0, 1]

for i in range(2, 41):
    fib[i] = fib[i-1] + fib[i-2]
    count[i][0] = count[i-1][0] + count[i-2][0]
    count[i][1] = count[i-1][1] + count[i-2][1]


t = int(input())
ans = [0, 0]
for _ in range(t):
    n = int(input())
    write(str(count[n][0]) + " " + str(count[n][1]) + "\n")