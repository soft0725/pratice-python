"""
a,b,c = [1, 2, 3]
print(a)
print(b)
print(c)

arr = "10 20 30".split()
print(arr)
print(list(map(int, arr)))
"""
# ----------------------------------

# numbers = input('숫자 3개 입력 : ')
# print(numbers.split()) 
# print(list(map(int, numbers.split())))
# a, b, c = (map(int, numbers.split()))
# print(f"{a}, {b}, {c}")
# print(f"{a+b+c}")

a,b,c = map(int, input("숫자 3개 입력 : ").split()[:3])
print(a+b+c) # 위와 똑같은 코드