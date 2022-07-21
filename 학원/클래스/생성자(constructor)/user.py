class User:
    username = None
    password = None
    name = None
    email = None

    def __init__(self, username, password, name, email):
        self.username = username
        print(self.username)
        print(self.password)
        print(self.name)
        print(self.email)
        print("-" * 10)
        print(username)
        print(password)
        print(name)
        print(email)
        print()
        print("생성자 호출?")

    def userInfo(self):
        print(self.username)
        print(self.password)
        print(self.name)
        print(self.email)

if __name__ == "__main__":
    user1 = User("bbb", "1111", "홍길동", "bbb@naver.com")

    user1.username = "aaa"
    user1.password = "1234"
    user1.name = "김병찬"
    user1.email = "byungchan0725@gmail.com"

    user1.userInfo()