# https://www.acmicpc.net/problem/2839

sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0: # 5의 배수라면
        bag += (sugar // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print("-1")