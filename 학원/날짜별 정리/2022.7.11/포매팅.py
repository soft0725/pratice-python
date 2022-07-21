# 포맷함수를 사용한 문자열 포매팅

name = "김병찬"
age = 17

strValue1 = "{0}님의 나이는 {1}입니다.".format(name,age)
print(strValue1)

strValue2 = f"{name}님의 나이는 {age}입니다." # f"~"는 3.~~이상부터 사용 가능 
# 모든 회사들은 최신 버전을 안씀 == 안정성 떨어짐 (버그 잦음) 그래서 2.~~대를 사용 
print(strValue2)

print("{0:<10}".format("hi"))