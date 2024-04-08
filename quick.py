import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # 리스트에서 임의의 피벗 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 입력 받기
N, K = map(int, input().split())  # N과 K를 공백을 기준으로 분리하여 입력받음
# 주어진 수열을 리스트로 저장
A = list(map(int, input().split()))

# 퀵 정렬을 사용하여 리스트 A를 정렬
sorted_A = quick_sort(A)

# 정렬된 리스트에서 K번째 있는 수 출력
print(sorted_A[K-1])  # 인덱스는 0부터 시작하므로 K번째 수는 인덱스 K-1에 위치함

