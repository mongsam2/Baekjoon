n = int(input())
numbers = list(map(int, input().split()))

def is_prime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

count = 0
primes = [2]
for num in numbers:
    if is_prime(num):
        count += 1
print(count)