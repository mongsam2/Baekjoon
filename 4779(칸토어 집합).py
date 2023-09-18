import sys
# k(): 문자열 리스트와 다룰 인덱스의 범위를 입력 -> 해당 범위를 3등분 후 가운데를 공백으로 변환
# -> 앞 부분 인덱스와 뒷 부분 인덱스의 범위 만큼 k() 호출 -> 인덱스의 범위가 1이 되면 호출중단
'''
def k(line, idx): # line은 리스트, idx는 튜플
    if idx[0]!=idx[1]:
        l = idx[1]-idx[0]+1
        k(line, (idx[0], idx[0]+l//3-1))
        k(line, (idx[1]-l//3+1, idx[1]))
        for i in range(idx[0]+l//3, idx[1]-l//3+1):
            line[i]=' '
while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        line = ['-']*3**n
        k(line, (0, len(line)-1))
        for l in line:
            print(l, end='')
        print()
    except ValueError:
        break
'''

def k(l):
    d = l//3
    if l==1:
        return '-'
    return k(d) +' '*d + k(d)

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        l = 3**n
        print(k(l))
    except ValueError:
        break