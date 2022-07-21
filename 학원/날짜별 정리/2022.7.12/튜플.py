from typing import Tuple


strTuple = (1, 2, 3, 4, 5)
strList = [1, 2, 3, 4, 5]

strList[2] = 30

# List는 대괄호 Tuple는 소괄호

print(strList)
# strTuple[2] = 30 은 에러가 뜬다.
# 이유로는 튜플은 처음 생성될 때 그 값에서 바뀌면 안된다. const 와 같은 것 같음 
# 지우기 넣기 안됨 
# 고유한 값을 사용해야 할 때 튜플을 사용함 

print(strTuple)

num = 10
num = 20

strTuple = (1, 2, 3) # 튜플의 값을 바꾸기 위해선 새로 튜플을 작성해야 함 
print(strTuple)

# 구조는 리스트와 같음 
# 튜플은 튜플 안에 튜플을 넣을 수 있고, 리스트도 안에 같이 넣을 수 있음 
# 인덱싱 사용 가능 슬라이싱 사용 가능 

# 튜플 더하기 가능 
Tuple1 = (1, 2, 3)
Tuple2 = (4, 5, 6)
temp = Tuple1 + Tuple2
print(temp)

print(type(strTuple))
print(type(strList))

strTuple = (1)
strList = [1]

print(type(strTuple)) # type이 tuple에서 int로 바뀌었음 
# 이유는 괄호만 써서 그럼
strTuple = (1,)
print(type(strTuple)) # 괄호에 숫자를 넣고 뒤에 , 을 붙이면 tuple로 나옴 
print(type(strList))
