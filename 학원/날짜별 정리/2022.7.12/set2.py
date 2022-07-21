s1 = set("hello, python")
s2 = set("hello, java")
s3 = set("javajavaaaa")

print(s1)
print(s3) # 중복이 제거 되서 출력됨 

# 교집합
r1 = s1 & s2
print(r1)
r1 = s1.intersection(s2) # 어렵더라도 명시적이라서 이것을 사용해야 함 
print(r1)

# 합집합
r2 = s1 | s2
print(r2)
r2 = s1.union(s2)
print(r2)

# 차집합
r3 = s1 - s2
print(r3)
r3 = s2 - s1
print(r3) # 반대가 되서 출력이 된다
r3 = s1.difference(s2)
print(r3)