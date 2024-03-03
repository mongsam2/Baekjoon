import sys
input = sys.stdin.readline

def recommend():
    h, w, n = map(int, input().split())
    order = []
    current = 0
    for room in range(1, w+1):
        for floor in range(1, h+1):
            order.append(floor*100 + room)
            current += 1
            if current == n:
                return order[n-1]
            
def recommend2():
    h, w, n = map(int, input().split())
    floor = str((n-1)%h + 1)
    room = str((n-1)//h + 1)
    ans = floor
    if len(room) == 1:
        ans = ans + "0" + room
    else:
        ans = ans + room
    return ans

t = int(input())
for _ in range(t):
    ans = recommend2()
    sys.stdout.write(ans+"\n")