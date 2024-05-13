# 아홉 난쟁이의 키 입력 받기
dwarfs = [int(input()) for _ in range(9)]

# 아홉 난쟁이의 키의 합 구하기
total_height = sum(dwarfs)

# 아홉 난쟁이 중에서 두 명의 키를 골라 키의 합이 100이 되도록 하기
for i in range(9):
    for j in range(i+1, 9):
        if total_height - (dwarfs[i] + dwarfs[j]) == 100:
            # 일곱 난쟁이의 키를 오름차순으로 정렬하고 출력
            result = sorted([d for k, d in enumerate(dwarfs) if k != i and k != j])
            for height in result:
                print(height)
            exit()
