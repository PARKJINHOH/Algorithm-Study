a = int(input())
b = int(input())
c = int(input())

value = list(str(a * b * c))  # value["1","7","0","3","7","3","0","0"]
for i in range(10):
    print(value.count(str(i)))
