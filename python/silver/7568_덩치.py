import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
people = []
for i in range(n):
    x, y = (map(int, input().split()))
    my_count = 1
    for p in people:
        if x>p[0] and y>p[1]:
            p[2] += 1
        elif x<p[0] and y<p[1]:
            my_count += 1
    people.append([x, y, my_count])
for i in people:
    write(str(i[2]) + " ")


