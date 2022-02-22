# https://www.acmicpc.net/problem/2675

rng = int(input())

for i in range(rng):
    cnt, word = input().split()
    result = ""
    for a in word:
        result = result + (a * int(cnt))
    print(result)