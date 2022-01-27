# https://www.acmicpc.net/problem/8958

cnt = int(input())

for i in range(cnt):
    value = 0
    result = 0
    quiz = list(input())
    for j in quiz:
        if j == "O":
            value = value + 1
            result = result + value
        else:
            value = 0
    print(result)
