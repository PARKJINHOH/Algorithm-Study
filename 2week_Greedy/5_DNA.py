n, m = map(int, input().split())

result = ''

A = 0
T = 0
G = 0
C = 0
dna = list()

# 입력
for _ in range(n):
    dna.append(list(input()))

# 리스트의 반만 검색해서 확인한다.
halfList = n / 2 + 1
halfList = int(halfList)
for i in range(0, n):
    print("i : ", i)
    for j in dna[i]:
        print("dna[i] : ", dna[i], " j : ", j, " i : ", i)
        if j == 'A':
            if A >= halfList:
                result += 'A'
                continue
            A += 1
        elif j == 'T':
            if T >= halfList:
                result += 'T'
                continue
            T += 1
        elif j == 'G':
            if G >= halfList:
                result += 'G'
                continue
            G += 1
        elif j == 'C':
            if C >= halfList:
                result += 'C'
                continue
            C += 1
print(result)
