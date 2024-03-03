import sys
input = sys.stdin.readline

def vps(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True


t = int(input())
for _ in range(t):
    line = input().strip()
    if vps(line):
        print("YES")
    else:
        print("NO")
