numbers = list(map(int, input().split()))

asc = [n for n in range(1, 9)]
desc = [n for n in range(8, 0, -1)]
if numbers == asc:
    print("ascending")
elif numbers == desc:
    print("descending")
else:
    print("mixed")
