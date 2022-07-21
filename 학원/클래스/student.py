"""
클래스명 : Student
변수
    studentCode - 학번
    studentName - 이름
    studentYear - 학년
    studentAddress - 주소
    studentPhone - 연락처

메소드
    studentInfo():
        학번 :
        이름 :
        학년 :
        주소 :
        연락처 :
"""

class Student:

    studentCode = None
    studentName = None
    studentYear = None
    studentAddress = None
    studentPhone = None

    def studentInfo(self):
        print(f"학번 : {self.studentCode}")
        print(f"학번 : {self.studentName}")
        print(f"학번 : {self.studentYear}")
        print(f"학번 : {self.studentAddress}")
        print(f"학번 : {self.studentPhone}")
        print()

if __name__ == "__main__":

    student1 = Student()
    student2 = Student()
    student3 = Student()

    student1.studentCode = "1101"
    student1.studentName = "강민석"
    student1.studentYear = "1학년"
    student1.studentAddress = "부산진구"
    student1.studentPhone = "010-1234-5678"

    student2.studentCode = "1102"
    student2.studentName = "김강민"
    student2.studentYear = "1학년"
    student2.studentAddress = "모름"
    student3.studentPhone = "010-2345-1234"

    student3.studentCode = "1103"
    student3.studentName = "김병찬"
    student3.studentYear = "1학년"
    student3.studentAddress = "부산진구"
    student3.studentPhone = "010-2114-6076"

    student1.studentInfo()
    student2.studentInfo()
    student3.studentInfo()

