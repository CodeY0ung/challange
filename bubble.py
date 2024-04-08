def bubble_sort(arr):
    n = len(arr)
    # 리스트를 순회하며 정렬을 수행
    for i in range(n):
        # 현재 원소와 다음 원소 비교하여 정렬
        for j in range(0, n-i-1):
            # 길이가 짧은 것부터 정렬, 길이가 같으면 사전 순으로 정렬
            if len(arr[j]) > len(arr[j+1]) or (len(arr[j]) == len(arr[j+1]) and arr[j] > arr[j+1]):
                # 두 원소의 위치를 바꿈으로써 정렬 수행
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 입력 받기
N = int(input("단어의 개수를 입력하세요: "))  # 단어의 개수 입력
words = [input(f"{i+1}번째 단어를 입력하세요: ") for i in range(N)]  # 단어 입력받아 리스트에 저장

# 중복 제거 후 버블 정렬
unique_words = list(set(words))  # 중복을 제거하기 위해 set을 사용하고, 다시 리스트로 변환
bubble_sort(unique_words)  # 정렬 함수 호출

# 정렬된 단어들 출력
for word in unique_words:
    print(word)  # 정렬된 단어들을 출력
