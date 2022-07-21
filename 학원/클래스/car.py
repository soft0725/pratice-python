"""
클래스 명 : Car
변수
    company - 회사명
    model - 모델명
    color - 색상

메소드
    carInfo()
        회사명:현대자동차
        모델명:쏘나타
        색상:화이트

현대자동차
쏘나타
화이트

기아
k5
블랙

기아
k8
그레이

"""
"""
class Car:

    company = None
    model = None
    color = None

    def carInfo(self):
        return self.company,self.model,self.color


car = Car()

car.company = "현대자동차"
car.model = "쏘나타"
car.color = "화이트"

print()
print(f"회사명 : {car.company}")
print(f"모델명 : {car.model}")
print(f"색상 : {car.color}")

car.company = "기아"
car.model = "K5"
car.color = "블랙"

print()
print(f"회사명 : {car.company}")
print(f"모델명 : {car.model}")
print(f"색상 : {car.color}")

car.company = "기아"
car.model = "K8"
car.color = "그레이"

print()
print(f"회사명 : {car.company}")
print(f"모델명 : {car.model}")
print(f"색상 : {car.color}")
"""

# 위는 내가 쓴 코드
# 아래는 선생님 코드

class Car:

    company = None
    model = None
    color = None

    def carInfo(self):
        print(f"회사명 : {self.company}")
        print(f"모델명 : {self.model}")
        print(f"색상 : {self.color}")
        print()

if __name__ == "__main__":
    c1 = Car()
    c2 = Car()
    c3 = Car()

    c1.company = "현대자동차"
    c1.model = "쏘나타"
    c1.color = "화이트"

    c2.company = "기아"
    c2.model = "K5"
    c2.color = "블랙"

    c3.company = "기아"
    c3.model = "K8"
    c3.color = "그레이"

    c1.carInfo()
    c2.carInfo()
    c3.carInfo()