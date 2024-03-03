import sys
m, n = map(int, input().split())
# 2, 3, 5, 7, 11, 13, 17, 19, 23


'''def update(prime):
    global is_prime
    global n
    pow = 2
    update_num = pow*prime
    while update_num <= n:
        is_prime[update_num] = False
        pow += 1
        update_num = pow*prime'''

is_prime = [True for _ in range(n+1)]

for num in range(2, n+1):
    if is_prime[num]:
        if num >= m:
            sys.stdout.write(str(num) + "\n")
        if num < n**0.5+1:
            for check in range(num*2, n+1, num):
                is_prime[check] = False


