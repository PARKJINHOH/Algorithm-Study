# https://www.acmicpc.net/problem/10250

num = int(input())
for _ in range(num):
    h, w, n = list(map(int, input().split()))

    front = n % h
    back = n // h + 1

    if front == 0:
        back = n // h
        front = h

    if back < 10:
        back = "0" + str(back)
    print(front, back, sep="")