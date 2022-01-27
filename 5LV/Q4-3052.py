# https://www.acmicpc.net/problem/3052

a = set()

for i in range(10):
    value = int(input())
    a.add(value % 42)

print(len(a))
