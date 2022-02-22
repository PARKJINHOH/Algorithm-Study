# https://www.acmicpc.net/problem/2941

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for alpa in croatia:
    word = word.replace(alpa, "1")
print(len(word))