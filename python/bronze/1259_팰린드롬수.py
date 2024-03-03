import sys
input = sys.stdin.readline

def is_pal(string):
    front = 0
    end = len(string)-1
    while front < end:
        if string[front] != string[end]:
            return False
        else:
            front += 1
            end -= 1
    return True

while True:
    num = input().strip()
    if num == "0":
        break
    if is_pal(num):
        sys.stdout.write("yes"+"\n")
    else:
        sys.stdout.write("no"+"\n")
    