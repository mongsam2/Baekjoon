moum = ['a', 'e', 'i', 'o', 'u']

def test(word):
    '''규칙에 모두 맞으면 True, 아니면 False'''

    moum_exist = False #모음이 최소 한 개 존재하는지
    moum_continue = 0 #모음이 몇 번 연속으로 있는지
    jaum_continue = 0 #자음이 몇 번 연속으로 있는지
    prev = "" # 이전 글자

    for letter in word: #한 글자씩 확인
        if not moum_exist and letter in moum:
            moum_exist = True

        if letter in moum:
            moum_continue += 1
            jaum_continue = 0
        elif letter not in moum:
            jaum_continue += 1
            moum_continue = 0
        if moum_continue == 3 or jaum_continue == 3:
            return False

        if letter not in ["e", "o"] and letter == prev:
            return False
        prev = letter

    if not moum_exist:
        return False
    else:
        return True

while True:
    word = input()
    if word == "end":
        break

    if test(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
    