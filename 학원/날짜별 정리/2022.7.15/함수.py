def add(a, b, c):
    print(f"a : {a}")
    if a == 10:
        return
    print(f"b : {b}")
    print()

result = add(10,20,30)
print(f"result : {result}")


def breakandreturn(list1):
    for num in list1:
        if num == 5:
            return
        print(num)
    print("함수 끝까지 실행됨")

numlist = list(range(1,11))

breakandreturn(numlist)