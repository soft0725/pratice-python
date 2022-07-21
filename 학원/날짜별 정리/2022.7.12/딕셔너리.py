# 딕셔너리의 개념은 Key와 Value로 나누어져 있음 
# 딕셔러니는 중괄호를 사용

strDict = {"이름":"김병찬", "나이":17}
strList = ["김병찬","17"]

# type 확인
print(type(strDict["이름"]))
print(type(strDict["나이"]))

# List와 Dict와 같은 출력 다른 방법이다.
print(strDict["이름"])
print(strDict["나이"]) 
print(strList[0])
print(strList[1]) 

# 딕셔너리에 값을 추가한다.
strDict["주소"] = "부산 부산진구"
print(strDict)

# List에 추가 (업핸드를 사용해야 한다.)
# strList[2] = 100
# print(strList)

# 딕셔너리에 값을 수정
strDict["나이"] = 20
print(strDict)

# Key값은 중복이 되지 않는다.
# 하지만 Value는 중복이 가능하다 

strDict["닉네임"] = "김병찬" # Value 값인 김병찬은 중복이 가능 
print(strDict)

# 딕셔너리 요소 삭제하는 법
del strDict["주소"] # Key 값과 Value 값이 한번에 날아가게 됨
print(strDict)

# 딕셔너리의 키값으로 쓸 수 없는 것 => List 
# 하지만 Tuple는 키 값으로 사용이 가능함 

# 리스트를 Key로 사용할 수 없는 이유 
strDict = {1:10, "김":"김병찬"}
print(strDict[1])
print(strDict["김"]) 

# strDict = {[10,20]:"리스트"}
# print(strDict[10,20])
# 위는 에러가 나는 것을 볼 수 있음 

# 리스트를 Tuple로 사용
strDict = {1:10, "김":"김병찬", (10,20):"리스트"}
print(strDict[10,20])
# 에러가 뜨지 않고 잘 나옴 
# 이유는 Tuple는 바뀌지 않는 고유한 값이기 때문에 가능
# 반명 List는 값이 바뀔 수도 있기 때문에 사용이 불가함 