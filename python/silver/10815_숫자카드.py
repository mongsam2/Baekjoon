import sys
write = sys.stdout.write

n = int(input())
my_cards = set(map(int, input().split()))
m = int(input())
query = list(map(int, input().split()))

for number in query:
    if number in my_cards:
        write("1 ")
    else:
        write("0 ")