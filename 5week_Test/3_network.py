# DFS / BFS 확인 문제

def solution(n, computers):

    def DFS(com):
        visited[com] = True

        for a in range(n):
            if computers[com][a] and not visited[a]:
                DFS(a)


    answer = 0
    # 방문 표시
    visited = [False for i in range(n)]

    for com in range(n):
        if not visited[com]:
            DFS(com)
            answer += 1

    return answer



n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n1, computers1))

n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n2, computers2))