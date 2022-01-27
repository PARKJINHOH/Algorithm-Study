# https://www.acmicpc.net/problem/4344

a = int(input())

for i in range(a):
    test_case = list(map(int, input().split()))
    students = test_case[0]
    score = test_case[1:]

    avg_score = sum(score) / students
    cnt = 0
    for j in score:
        if j > avg_score:
            cnt = cnt + 1
    print(format(round(cnt / students * 100, 3), ".3f") + "%")


