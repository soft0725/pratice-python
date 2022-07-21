numbers = list() # 비어있는 List

"""
반복할 횟수를 입력하세요 : 10
list에 1 ~ 10까지가 들어감 
"""

len = int(input("반복할 횟수를 입력해 주세요 : "))

i = 1
while i <= len:
    numbers.append(i)
    i += 1

print(f"리스트 : {numbers}") 

i = 0
numbers.clear()

while i < len:
    numbers.append(len - i)
    i = i + 1

print(f"리스트 : {numbers}")