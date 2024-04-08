# 입력 받기
N, K = map(int, input().split())  # N과 K를 공백을 기준으로 분리하여 입력받음
# 주어진 수열을 리스트로 저장
A = list(map(int, input().split()))

# 주어진 리스트 A를 오름차순으로 정렬
A.sort()

# 정렬된 리스트에서 K번째 있는 수 출력
print(A[K-1])  # 인덱스는 0부터 시작하므로 K번째 수는 인덱스 K-1에 위치함
