from re import A


str1 = "Python"
str2 = "good"
str3 = str1 + str2
print(str3) # 파이썬에서는 문자열을 더할 수 있음

print(str1 * 2)  #문자열을 2번 출력하라는 뜻임 

print(len(str1)) # str1의 문자열 길이 

# 문자열을 리스트로 변환하는 방법 

a = "pithon" # a의 1번방 i를 수정하려면 list로 만들어 줘야함 
b = list(a) # b를 리스트로 만들어서 a의 값을 넣어줌 

# 리스트로 바뀐 문자열 1번 인덱스의 값에 y 대입
b[1] = 'y'

a = ''.join(b) # join은 합쳐주는 것 출력하면 Python
# '/'.join(b) 은 리스트 사이에 /를 넣고 P/y/t/h/o/n이 출력됨.

print(a)

# 문자열 포매팅
print("I eat %d apples." % 3) # %d에 3이 들어감 (정수형)

print("I eat %s apples." % "five") # %s에 five가 들어감 (문자형)

name = "김병찬"
age = 17

strValue1 = '%s님의 나이는 %s 입니다.' %(name,age) # ()로 묶지 않으면 값이 2개이기 때문에 에러가 뜸, 1개는 () 안해도 가능 
strValue2 = name + "님의 나이는 " + str(age) + " 입니다."
# 같은 출력 값이지만 다른 코드 
print(strValue1) 
print(strValue2)

strValue3 = name, "님의 나이는", age, "입니다." # 튜플 
print(strValue3)
print(name, "님의 나이는", age, "입니다.") # ,는 알아서 변수를 더해주고 띄어줌 
