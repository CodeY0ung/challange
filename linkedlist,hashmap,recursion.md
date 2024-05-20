1. 링크드 리스트 (Linked List)
링크드 리스트는 각 요소가 데이터와 다음 요소에 대한 참조를 포함하는 노드들로 구성된 자료 구조입니다.
단일 링크드 리스트: 각 노드가 다음 노드를 가리키는 링크를 가지고 있습니다.
이중 링크드 리스트: 각 노드가 다음 노드와 이전 노드를 가리키는 두 개의 링크를 가지고 있습니다.
동적 크기 조절: 배열과 달리 크기를 미리 지정하지 않아도 됩니다.
삽입과 삭제가 용이: 리스트의 중간에 삽입하거나 삭제하는 작업이 비교적 간단합니다.
장점:
삽입/삭제가 빠릅니다 (리스트 중간에서의 작업).
크기 조절이 필요 없습니다.
단점:
임의 접근이 불가능하여 탐색 시간이 오래 걸립니다.
추가적인 메모리가 필요합니다.
백준 1158 - 요세푸스 문제
import sys
input = sys.stdin.readline 

# 입력 받기: n은 사람의 수, k는 제거할 사람의 순번
n, k = map(int, input().split())

# 1부터 n까지의 숫자를 가진 리스트 생성 (원형 리스트를 구현하기 위해)
circle = [i for i in range(1, n + 1)]
result = []  # 요세푸스 순열을 저장할 리스트
num = k - 1  # 첫 번째 제거될 사람의 인덱스 (0부터 시작하므로 k-1)

# 모든 사람이 제거될 때까지 반복
while len(circle):
    if num >= len(circle):
        # 현재 인덱스가 리스트의 길이보다 크거나 같으면 리스트의 길이로 나눠 순환
        num = num % len(circle)
    else:
        # 현재 인덱스에 해당하는 사람을 결과 리스트에 추가하고 circle 리스트에서 제거
        result.append(str(circle.pop(num)))
        # 다음 제거될 사람의 인덱스 계산 (현재 인덱스에 k-1을 더함)
        num += k - 1

# 결과를 형식에 맞게 출력
print("<", ", ".join(result), ">", sep='')


2. 해시 맵 (Hash Map)
해시 맵은 키와 값을 연결하는 데이터 구조입니다.
해시 함수를 사용하여 키를 배열의 인덱스로 변환하고, 해당 위치에 값을 저장합니다.
빠른 데이터 접근: 키를 통해 상수 시간 복잡도로 값을 검색할 수 있습니다.
키-값 쌍으로 데이터 저장.
장점:
빠른 검색, 삽입, 삭제가 가능합니다.
단점:
충돌이 발생할 수 있습니다.
해시 함수의 성능에 따라 효율이 달라집니다.
백준 - 1764 듣보잡 

import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

# n, m은 각각 듣도 못한 사람의 수와 보도 못한 사람의 수
n, m = map(int, input().split())

a = set()  # 듣잡 이름 집합
b = set()  # 보잡 이름 집합
result = []  # 듣도 보도 못한 사람들의 이름을 저장할 리스트

# 듣잡 이름을 입력 받아 집합 a에 추가
for _ in range(n):
    a.add(input().strip())  # 줄바꿈 문자 제거를 위해 .strip() 사용

# 보잡 이름을 입력 받아 집합 b에 추가
for _ in range(m):
    b.add(input().strip())  # 줄바꿈 문자 제거를 위해 .strip() 사용

# 집합 a에 있는 이름들 중 집합 b에도 있는 이름을 찾아 result 리스트에 추가
for i in a:
    if i in b:
        result.append(i)

# 결과 리스트를 사전순으로 정렬
result.sort()

# 듣보잡 사람 수 출력
print(len(result))

# 듣보잡 사람의 이름을 한 줄씩 출력
for i in result:
    print(i)


3. 재귀 (Recursion)
재귀는 함수가 자기 자신을 호출하는 프로그래밍 기법입니다.
재귀는 보통 종료 조건(base case)과 재귀 호출로 구성됩니다.
문제를 더 작은 문제로 나누어 해결.
종료 조건이 중요함 (없으면 무한 루프에 빠짐).
장점:
코드가 간결하고 이해하기 쉬울 수 있습니다.
문제를 자연스럽게 분할하여 해결할 수 있습니다.
단점:
재귀 호출이 많아지면 스택 오버플로우가 발생할 수 있습니다.
반복문에 비해 성능이 떨어질 수 있습니다.
백준 2447번 - 별 찍기
def draw_stars(n):
    if n == 1:
        return ["*"]  # 기본 패턴: 크기 1일 때의 별 하나

    # 크기 n//3인 작은 패턴 가져오기
    stars = draw_stars(n // 3)
    result = []

    # 크기 n 패턴을 만들기 위해 작은 패턴을 3x3 배열로 복사
    for s in stars:
        result.append(s * 3)  # 첫 번째 줄: 작은 패턴을 가로로 세 번
    for s in stars:
        result.append(s + ' ' * (n // 3) + s)  # 중간 줄: 작은 패턴, 공백, 작은 패턴
    for s in stars:
        result.append(s * 3)  # 마지막 줄: 작은 패턴을 가로로 세 번

    return result

# 입력 받기
n = int(input())
result = draw_stars(n)
print("\n".join(result))  # 결과 출력
