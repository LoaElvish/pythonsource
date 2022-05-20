# 연산자
# 산술연산자 : +, -, *, /(실수), //(정수), %, **(승수)
a, b = 5, 3
print(a+b,a-b,a*b,a/b,a//b,a**b)

print()
s1,s2,s3 = "100","100.123","999999999"
print(s1+s2+s3) # + : 연결 => 100100.123999999999
print(float(s1)+float(s2)+float(s3)) # 1000000199.123
print(int(s1) + 1) #TypeError: can only concatenate str (not "int") to str

# 복합대입연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a -= 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)

# 실습 : 777,777원
# 화폐교환 : 5만원/1만원/5천원/1천원

# won = 777777
# m50000 = won // 50000
# won %= 50000
# m10000 = m50000 // 10000 
# won %= 10000
# m5000 = m10000 // 5000 
# won %= 5000
# m1000 = m5000 // 1000 
# won %= 1000


# 관계연산자 : ==, !==, >, <, >=, <=
a,b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리 연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15)
print(100 > 60 or 60 < 15)
print(not 60 < 15)
print(not True)
print(not False)
# print(!True)

# 비트 연산자
print(10 & 7)
print(10 | 7)
print((100 > 60) & (60 > 15))

