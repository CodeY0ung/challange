import random

# 퀵 정렬 함수 정의
def quick_sort(arr):
    # 리스트의 길이가 1 이하인 경우에는 그대로 반환
    if len(arr) <= 1:
        return arr
    # 리스트에서 임의의 피벗 선택
    pivot = random.choice(arr)
    # 피벗을 기준으로 작은 값, 같은 값, 큰 값으로 분류
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # 분류된 리스트들을 재귀적으로 정렬 후 합치기
    return quick_sort(left) + middle + quick_sort(right)

# 입력 받기
N, K = map(int, input("N과 K를 공백을 기준으로 입력하세요: ").split())  # N과 K를 공백을 기준으로 분리하여 입력받음
# 주어진 수열을 리스트로 저장
A = list(map(int, input("수열을 입력하세요: ").split()))

# 퀵 정렬을 사용하여 리스트 A를 정렬
sorted_A = quick_sort(A)

# 정렬된 리스트에서 K번째 있는 수 출력
print(sorted_A[K-1])  # 인덱스는 0부터 시작하므로 K번째 수는 인덱스 K-1에 위치함
