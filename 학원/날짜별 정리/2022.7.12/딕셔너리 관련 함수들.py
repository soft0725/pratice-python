strDict = {"이름":"김병찬", "나이":17}

# key값만 list로 추출 
print(strDict.keys())
print(list(strDict.keys())) # 앞에 list를 추가하면 list처럼 보여줌 

# values값만 list로 추출 
print(strDict.values()) # 똑같이 list로 쓰고 싶다면 위처럼 쓰면 된다
print(list(strDict.values()))

# key, value값 둘다 tuple로 묶어서 추출 (tuple 형식으로 출력이 된다)
print(strDict.items()) # key와 value가 묶여서 출력이 된다.
print(list(strDict.items())) 

# 딕셔너리 전체를 지우는 함수 
# strDict.clear() 딕셔너리 전체가 지워짐
print(strDict)

print(strDict["이름"])
print(strDict.get("이름")) # 위와 똑같이 출력이 된다. (같은 출력 다른 방법)
# 둘중에 뭘 써야하나?
# get을 써야함 

strDict.update({"이름":"김병찬"}) # update는 값을 추가 또는 값이 있다면 수정 
print(strDict)
strDict.update({"주소":"부산"})
print(strDict)

# 해당 key가 딕셔너리 안에 있는지 조사하기 
strDict = {"이름":"김병찬","주소":"부산"}
print("이름" in strDict) # true를 출력 
print("나이" in strDict) # false를 출력

# print(strDict.popitem()) # 제일 끝에 있는 아이템 하나를 꺼낸다.
# print(strDict.pop()) # key값을 통해서 값을 꺼낸다.