# 시간초과 문제 발생
# 리스트에서는 어떤 값이 리스트에 있는지 확인하려면 리스트의 값을 일일이 확인해야 한다.
# 해시 테이블로 구현되어 있는 set의 경우, 해당 값을 해시 함수에 넣어 인덱스에 접근,
# 평균 시간 복잡도는 O(1) 리스트는 O(n)

# ** 중복되지 않는 값을 저장할 때는 리스트보다 set을 사용하는게 더 효율적이다.
import sys
n = int(input())
lst=set() #회사에 있는 사람의 목록
for _ in range(n):
    log = sys.stdin.readline().rstrip().split()
    name, record = log
    if record == "enter": # 출근
        lst.add(name)
    else: # 퇴근
        lst.remove(name)
lst = list(lst) #정렬을 위해 리스트로 변환
lst.sort(reverse=True) # 리스트를 역순으로 정렬
for name in lst:
    sys.stdout.write(name+'\n')