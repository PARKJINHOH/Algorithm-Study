def hanoi(num, rod1, rod2, rod3):
    if num == 1:
        print(rod1, rod3)

    else:
        hanoi(num - 1, rod1, rod3, rod2)
        print(rod1, rod3)
        hanoi(num - 1, rod2, rod1, rod3)


num = int(input())
print(2 ** num - 1)
hanoi(num, 1, 2, 3)



