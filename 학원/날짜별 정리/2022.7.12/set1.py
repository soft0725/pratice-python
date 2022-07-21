# 집합 자료형의 특징
# 중복을 허용하지 않는다
# 순서가 없다
# 딕셔너리랑 set은 겹친다. 그래서 set을 사용하려면 set을 붙여줘야함 
# set보다는 딕셔너리가 더 중요함! 

strSet = set([1,2,3,4])
print(strSet)

a = {}
print(type(a))
b = set()
print(type(b))

print(a)
print(b)

# set은 인덱싱을 사용할 수 없다.
# print(strSet[0])  
# set에서 인덱싱을 사용할려면 list를 사용
print(list(strSet)[0])