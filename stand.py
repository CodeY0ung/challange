import sys
input = sys.stdin.readline  # 입력 속도를 빠르게 하기 위해 사용하는 방법

a, b = map(int, input().split())  # 영학이의 패 입력받기
total = 9 * 17  # 전체 경우의 수 계산
ans = 0  # 이길 확률 초기화

if a == b:  # 땡인 경우
    ans = total - (10 - a)  # 땡인 경우는 땡을 제외한 모든 경우에서 이길 수 있음
else:  # 끗인 경우
    mypoint = (a + b) % 10  # 영학이의 패의 끗 계산
    for i in range(1, 11):  # 각각의 끗에 대해
        for j in range(i + 1, 11):
            if mypoint > (i + j) % 10:  # 영학이가 이길 수 있는 경우
                if i == a and j == b:  # 상대방의 패와 같은 경우는 제외
                    continue
                elif i == a or j == a or i == b or j == b:  # 영학이의 패가 있는 경우
                    ans += 2  # 이길 확률 추가
                else:  # 영학이의 패가 없는 경우
                    ans += 4  # 이길 확률 추가

print("%.3f" % (ans / total))  # 이길 확률 출력, 소수점 아래 세 자리까지
