from collections import deque

# 재귀를 사용한 DFS 함수
def dfs(start):
    visited[start] = True  # 현재 노드를 방문했음을 표시
    print(start, end=" ")  # 현재 노드를 출력

    # 현재 노드와 연결된 모든 노드에 대해
    for i in graph[start]:
        if not visited[i]:  # 아직 방문하지 않은 노드라면
            dfs(i)  # 해당 노드를 시작으로 DFS 수행

# 큐를 사용한 BFS 함수
def bfs(start):
    queue = deque([start])  # 시작 노드를 큐에 삽입
    visited[start] = True  # 시작 노드를 방문했음을 표시

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 노드를 하나 꺼내옴
        print(v, end=" ")  # 꺼낸 노드를 출력

        # 꺼낸 노드와 연결된 모든 노드에 대해
        for i in graph[v]:
            if not visited[i]:  # 아직 방문하지 않은 노드라면
                visited[i] = True  # 해당 노드를 방문했음을 표시
                queue.append(i)  # 해당 노드를 큐에 삽입

# 정점의 개수(N), 간선의 개수(M), 시작 정점(V)을 입력 받음
N, M, V = map(int, input().split())

# 그래프를 인접 리스트 형태로 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보를 입력 받아 그래프에 저장
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 인접 리스트를 정렬하여 방문 순서가 작은 노드부터 방문하도록 함
for i in graph:
    i.sort()

# DFS 수행을 위한 방문 여부 리스트 초기화
visited = [False] * (N + 1)

# 시작 노드를 기준으로 DFS 수행
dfs(V)
print()  # 줄 바꿈

# BFS 수행을 위한 방문 여부 리스트 초기화
visited = [False] * (N + 1)

# 시작 노드를 기준으로 BFS 수행
bfs(V)
