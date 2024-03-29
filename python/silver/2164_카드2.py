from collections import deque

def update_que(q):
    q.popleft()
    a = q.popleft()
    q.append(a)

n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) > 1:
    update_que(q)
print(q[0])

'''
파이썬의 collections 모듈에 있는 deque (덱, 더블 엔디드 큐)는 양쪽 끝에서 데이터를 추가하거나 제거할 수 있는 일종의 큐입니다. 이는 리스트와 비슷하지만, deque는 양쪽 끝에서의 데이터 처리가 매우 효율적이라는 점에서 차이가 있습니다. 파이썬의 deque는 동적 배열이나 연결 리스트와는 다른 방식으로 구현되어 있으며, 그 구현은 CPython의 _collectionsmodule.c 소스 코드에서 확인할 수 있습니다.

구현 방식
deque의 내부 구현은 일종의 동적 배열을 사용하는데, 이는 "블록"이라 불리는 작은 단위의 배열들을 연결 리스트처럼 연결하여 사용합니다. 각 블록은 여러 개의 요소를 저장할 수 있는 고정 크기를 가지며, deque 전체는 이런 블록들의 연결로 이루어져 있습니다. 이 구조 덕분에 deque는 앞뒤 양쪽에서의 요소 추가 및 제거를 O(1) 시간 복잡도로 수행할 수 있습니다.

주요 특징
양쪽 끝에서의 효율적인 연산: deque는 앞쪽과 뒷쪽 양쪽에서 요소를 추가하거나 제거하는 연산을 매우 빠르게 수행할 수 있습니다.
동적 크기 조정: 내부적으로 블록들을 추가하거나 제거함으로써, deque는 필요에 따라 동적으로 크기를 조정할 수 있습니다.
메모리 사용 최적화: 연결 리스트에 비해, deque는 메모리 사용량을 줄이면서도 빠른 인덱스 접근을 제공합니다. 각 블록은 고정 크기의 배열로, 메모리를 효율적으로 사용하면서도 빠른 접근 속도를 제공합니다.
구현 세부 사항
블록 연결: 내부적으로 deque는 각 블록을 양방향 연결 리스트로 연결합니다. 이는 각 블록의 시작과 끝에 포인터를 두어, 이전 및 다음 블록을 가리키도록 함으로써 이루어집니다.
데이터 추가 및 제거: 데이터를 deque의 앞이나 뒤에 추가할 때, 해당 방향의 끝 블록에 공간이 있는지 확인합니다. 충분한 공간이 있다면, 데이터를 추가하고, 그렇지 않다면 새로운 블록을 할당하여 데이터를 추가합니다. 데이터 제거도 비슷한 방식으로 이루어집니다.
자동 크기 조정: deque는 요소가 추가되거나 제거됨에 따라 필요에 따라 자동으로 크기를 조정합니다. 이는 내부적으로 더 많은 블록을 할당하거나 불필요한 븜ㄱ을 제거함으로써 이루어집니다.
파이썬의 deque는 이러한 구현 덕분에 높은 성능을 유지하면서도 다양한 사용 사례를 지원합니다. 예를 들어, 스택이나 큐의 기능을 필요로 하는 경우, 또는 양쪽 끝에서의 빈번한 추가 및 제거 연산이 필요한 경우에 매우 유용합니다.
'''