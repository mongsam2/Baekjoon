import sys
input = sys.stdin.readline
write = sys.stdout.write

def check(s):
    stack = []
    for letter in s:
        if letter == "(" or letter == "[":
            stack.append(letter)
        elif letter == ")" or letter == "]":
            if len(stack) == 0:
                return False
            if (letter == ")" and stack[-1] == "(") or (letter == "]" and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(letter)
    if len(stack) == 0:
        return True
    else:
        return False

while True:
    s = input().rstrip()
    if s == ".":
        break
    if check(s):
        write('yes\n')
    else:
        write('no\n')