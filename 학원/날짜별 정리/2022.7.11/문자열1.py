from dataclasses import replace
from pickletools import stringnl


strValue = "hello, python"

# 문자열에 해당 문자가 몇개인지 확인하는 함수 
print(strValue.count("l")) # l이 몇개있는지 체크함 

a = "life is too short"
print(a.find('t')) # 찾는 값이 없어도 될때 쓰는게 좋음 만약 없다면 -1을 출력 
print(a.index('t')) # 무조건 찾는 값이 있어야 할때 쓰는 것이 좋음 만약 없다면 에러

# 문자열 삽입
print(",".join('abcd')) # 문자열 사이 사이에 , 를 추가함 
print(",".join(['a','b','c','d'])) # 리스트도 다른건 없음 

jStrValue = "/".join(strValue)
print(jStrValue) # 문자열을 토큰으로 나눠야 될때 사용함 
# 제일 많이 쓰이는 것은 list를 합칠때 가장 많이 사용함 

strList = ["100","200","300","400"]
strList2 = [100,200]
print(" ".join(strList)) # 위에 list는 int형 이기 때문에 문자열 형식으로 바꿔주어야 join이 가능함 

# strList2에 들어 있는 정수(int) 자료형의 값들을 문자열로 변환 
print(list(map(str, strList2)))
# strList2에 들어 있는 문자열(string) 자료형의 값들을 정수로 변환 
print(list(map(int, strList)))

# 문자열의 양쪽 끝에 있는 공백을 제거 
strValue = " 코리아 아카데미 "
print(strValue.strip()) # 양쪽의 공백이 사라짐 
print(strValue.lstrip()) # 왼쪽의 공백이 사라짐 
print(strValue.rstrip()) # 오른쪽의 공백이 사라짐 

# 문자열에서 해당 문자열을 찾아서 다른 값으로 바꿔라 
strValue2 = "코리아 아카데미"
print(strValue2.replace(" ","")) # strValue2 에서 공백인 부분을 찾아서 공백을 없애라 
phoneNumber = "010-1234-5678"
print(phoneNumber.replace("-","")) # -을 찾아서 ""로 바꿔라 

# 문제

# 1 내가 푼 문제 코드 
address = " 부산광역시 동래구 사직동 "
address1 = " 부산광역시 동래구 사직동 "
# 출력결과 : 부산-동래-사직
address = address.strip() # 1. 양쪽 공백 제거 
address = address.replace(" ","-") # 2. 공백을 -로 바꿔줌 
address = address.replace("부산광역시","부산") # 
address = address.replace("동래구","동래")
address = address.replace("사직동","사직")
print(address)

# 2. 선생님이 푸신 정답 코드
address1 = address1.split() # 리스트로 바꿔줌 
address1[0] = address1[0].replace("광역시","")
address1[1] = address1[1].replace("구","")
address1[2] = address1[2].replace("동","")
address1 = "-".join(address1)
print(address1)
