# https://www.acmicpc.net/problem/5622

alphabet_list = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = list(input())
time = 0

for w in word:
    for a in alphabet_list:
        if w in a:
            time = time + alphabet_list.index(a) + 2
print(time)