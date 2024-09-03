import sys
from collections import deque
from math import inf
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

all_chickens = []
all_houses = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            all_chickens.append((i, j))
        elif board[i][j] == 1:
            all_houses.append((i, j))

def get_distance(chicken_lst): # [(i, j, dist)]
    global all_houses
    total_dist = 0
    for house in all_houses:
        min_distance = inf
        for chicken in chicken_lst:
            distance = abs(house[0]-chicken[0])+abs(house[1]-chicken[1])
            if distance < min_distance:
                min_distance = distance
        total_dist += min_distance
    return total_dist

all_cases = combinations(all_chickens, m)
#print(list(all_cases))

min_answer = inf
for chicken_lst in all_cases:
    distance = get_distance(chicken_lst)
    if distance < min_answer:
        min_answer = distance

print(min_answer)