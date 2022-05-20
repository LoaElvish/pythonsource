# while : tab 같은 블럭임을 표시해야 함

# 1 ~ 10 출력
i = 1 # 초기값
while i < 10 : #조건
    print(i, end =" ")
    i = i + 1 # 증감

print()
# 1 ~ 100 짝수만 출력
i = 2
while i <= 100:
    print(i, end=" ")
    i += 2

print()
# 1 ~ 100 홀수만 출력
i = 1
while i < 100:
    print(i, end=" ")
    i += 2

print()
# i는 1씩 증가 /if 문 사용 1~100 홀수 입력
i = 1
while i < 101:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1

print()

# 1~100까지 합계 출력
i = 1
sum1 = 0
while i < 101:
    sum1 += i
    i += 1
print("1~100 합계 : ",sum1)    

# sum() 함수
# range(시작숫자, 끝나는 숫자, 증감값)
print(sum(range(1,101)))

print()
# 3단 출력
i = 1
while i < 10:
    print('%d X %d = %d' % (3, i, (3*i)))
    i += 1

print()
i = 1
while i < 9:
    i += 1
    j = 1
    while j < 10:
        print(i, "X", j, "=" ,j*i)
        j += 1
    
    



