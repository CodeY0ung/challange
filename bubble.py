def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 한 번의 순회에서 어떤 원소도 위치를 바꾸지 않으면 이미 정렬된 상태이므로 종료
        swapped = False
        for j in range(0, n-i-1):
            # 길이가 짧은 것부터 정렬, 길이가 같으면 사전 순으로 정렬
            if len(arr[j]) > len(arr[j+1]) or (len(arr[j]) == len(arr[j+1]) and arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 두 원소의 위치를 바꿈으로써 정렬 수행
                swapped = True
        if not swapped:
            break  # 한 번의 순회에서 어떤 원소도 위치를 바꾸지 않았으면 이미 정렬된 상태이므로 종료

# 입력 받기
N = int(input())  # 단어의 개수 N 입력
words = [input() for _ in range(N)]  # N개의 단어 입력받아 리스트에 저장

# 중복 제거 후 버블 정렬
unique_words = list(set(words))  # 중복을 제거하기 위해 set을 사용하고, 다시 리스트로 변환
bubble_sort(unique_words)  # 정렬 함수 호출

# 정렬된 단어들 출력
for word in unique_words:
    print(word)  # 정렬된 단어들을 출력
