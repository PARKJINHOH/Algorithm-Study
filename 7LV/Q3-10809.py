# https://www.acmicpc.net/problem/10809

a = input()
alphabet = list(range(97, 123)) # 아스키코드 a ~ z

for i in alphabet:
    print(a.find(chr(i)))

