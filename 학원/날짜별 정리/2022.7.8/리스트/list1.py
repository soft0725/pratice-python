numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers)

# 인덱싱 [위치 번호] : 위치 번호는 0부터 시작한다.
# 리스트나 튜플, 문자열에서 특정 위치의 값을 참조할 때 
# 사용한다.
print(numbers[0])
print(numbers[4])  

# 슬라이싱 [시작 위치 번호 : 마지막 위치 다음번호]
# 리스트나 튜플, 문자열에서 해당 범위의 값을 
# 모두 참조할 때 사용한다.
print(numbers[1:5]) # 1부터 5 전 까지
print(numbers[3:]) # 3부터 마지막 까지 
print(numbers[:5]) # 처음부터 5 전 까지 

# 역순 인덱싱, 슬라이싱 
print(numbers[-1]) # 0번방에서 -1 번방은 0번방에서 뒤로 한칸
print(numbers[-4:-1]) 
print(numbers[:-3])
print(numbers[-5:-2])


# 다양한 형태의 값을 저장하는 리스트 

list1 =  [10, "김병찬", 3.14, [1,2,3,4], 5] 

list2 = list1[3] # list1[3][2] 같음

print(list1[3][1:3]) # 슬라이싱도 가능함 

# list3 = [1, 2, ['a', 'b', ['hi', 'name']]] 3중 리스트

# 연산 사용하기 ( +, * ) 
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
list3 = list1 + list2
print(list3)



list4 = list1 * 3
print(list4)

# 리스트, 튜플, 문자열, 딕셔너리 자료형들의 길이(크기)
# 구해주는 함수 len()

list1_size = len(list1)
list2_size = len(list2)
list3_size = len(list3)
list4_size = len(list4)

print(list1_size)
print(list2_size)
print(list3_size)
print(list4_size)

# 값 수정 
list1 = [1, 2, 3]
list1[0] = 10
list1[1] = 20
list1[2] = 30
print(list1)

# 값 삭제
del list1[1]
print(list1)

# 함수를 사용하는 방법 
list1 = [1, 2, 3]
list1.append(4) # append는 제일 마지막에 추가하라라는 의미를 가지고 있음
print(list1)

num1 = list1.pop(1) # 해당 인덱스의 값을 꺼내라라는 뜻을 가지고 있다 
num1 = list1.pop() # pop에 인덱스를 넣지 않으면 마지막 값을 꺼낸다
print(list1) 
print(num1)

# del list1[0] remove와 같은 역할 이지만 remove는 해당 값을 찾는 것이고, del은 해당 인덱스를 찾아서 제거하는 것이다.

list1.remove(3) # 해당 값을 찾아서 제거해라 
print(list1)

list1.insert(1, 10) # (a, b)에서 a번의 위치에 b의 값을 넣고 뒤로 밀어 버린다.
list1.insert(1, 20)
print(list1)

list1 = [1, 5, 3, 7, 4]
list1.sort() # sort는 뜻이 정렬하라는 뜻
print(list1)

list1.reverse() # reverse는 sort와 다르게 거꾸로 큰 순서대로 정렬하는 함수이다 
                # 다만 정렬이 되는 것은 아니다 
                # list1를 정렬하지 않았으면 4 7 3 5 1로 출력된다
                # 그냥 반전의 역할
print(list1)

list1.clear() # list1을 비운다
print(list1)

list1 = [1, 1, 1, 1, 2, 3, 4, 4, 4]
num1Count = list1.count(1) # 리스트에서 해당 값의 개수를 카운트한다
print(num1Count)

num2Index = list1.index(2) # index(n) n의 위치를 알려준다
print(num2Index)

num2Index = list1.index(1) # 만약 해당 값이 중복이 된다면 가장 빠른 값의 위치를 알려준다
print(num2Index)

list2 = list1.copy()  # 깊은 복사 : 주소안에 있는 모든 값을 복사 
list1.remove(2)
print(list1)
print(list2)

list3 = list1         # 얕은 복사 : 주소만 복사 
list1.remove(3)
print(list1)
print(list3)

list1.extend([8, 8, 8, 8]) # 리스트에 리스트 더하기  
# 위의 extend를 생략한 코드는 아래코드와 같다
# list1 = list1 + [8 , 8, 8, 8]
print(list1)

str1 = "abcdefg"
print(str1[1:4])