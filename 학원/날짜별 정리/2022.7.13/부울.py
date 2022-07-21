#print(10 > 5 and 10 > 10)
#print(10 > 5 or 10 > 10)
#print(10 > 5 and not(10 > 10))

# 부울 연산

# True = 1, False = 0

# and(&) - 곱
# True and True  => True 
# True and False => False 
# False and False => False 
print(True and True)
print(True and False)
print(False and False)


# or(|) - 합 
# True or True => True
# True or False => True 
# False or False => False 
print(True or True)
print(True or False)
print(False or False)


# not(!) - 부정 
# not True => False 
# not False => True 
print(not True)
print(not False)


# 윤달
# 해당 년도가 4의 배수이면서 100의 배수는 아니거나 400의 배수일 때 

year = 2000
print((year%400==0) and (year%100!=0 or year%400==0))

'''
and연산은 모든 조건이 참일 때만 True이다
하나라도 False면 결과는 False

or연산은 모든 조건이 거짓일 때만 False이다
하나라도 True면 결과는 True
'''