n, m = map(int, input().split())
weight = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i + 1, n):
        if weight[i] != weight[j]:
            result += 1
print(result)



