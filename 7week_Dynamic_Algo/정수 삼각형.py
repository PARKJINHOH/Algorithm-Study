# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0: # 삼각형 왼쪽 끝인 경우
                triangle[i][j] += triangle[i - 1][j]
            elif j == i: # 삼각형 오른쪽 끝인 경우
                triangle[i][j] += triangle[i - 1][j - 1]
            else: # 양끝이 아닐 경우
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])
    return max(triangle[-1])
