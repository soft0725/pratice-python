# 대입 연산자 
name = "김병찬"

# 산술 연산자
result = 10 + 2
result = 10 - 2
result = 10 * 2
result = 10 / 2
result = 10 // 2
result = 10 % 2
result = 10 ^ 2
result = 10 ** 2

# 부호 연산자 
num = +1
num = -1

# 비교 연산자 
print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 == 5)
print(10 != 5)

# 논리 연산자 
print(True and False)
print(True or False)
print(not (True or True))

# 복합대입 연산자 (산술 연산 모두 사용 가능)
num = 10
num = num + 5
num += 5

num %= 5

# 삼항(조건) 연산자 
result = 0 if 10 > 5 else 1

year = 2000
result = print('윤년입니다') if (year%4==0 and (year%100!=0 or year%400==0)) else print('윤년이 아닙니다')
