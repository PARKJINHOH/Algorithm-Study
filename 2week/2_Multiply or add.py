number = input()

result = 0

for i in list(map(int, number)):
    if i <= 1:
        result += i
    else:
        if result == 0:
            result = i
        else:
            result *= i

print(result)
