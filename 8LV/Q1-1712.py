# https://www.acmicpc.net/problem/1712

a, b, c = list(map(int, input().split()))

profit = c - b

result = 0
if profit <= 0:
    print(-1)
else:
    result = a // profit
    print(result + 1)