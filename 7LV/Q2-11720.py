# https://www.acmicpc.net/problem/11720

a = input()
num = list(input())

result = 0
for i in num:
    result = result + int(i)
print(result)