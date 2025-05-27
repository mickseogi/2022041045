##################
# 프로그램명: 성적처리 프로그램 DB 연동
# 작성자: 2022041045 서민석
# 작성일: 2025. 05. 27
##################


import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='smsdneft1!',
    db='student_db',
    charset='utf8'
)
cursor = conn.cursor()

STUDENTS = 5

class Student:
    def __init__(self, id, name, eng, c, py):
        self.id = id
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.total = self.calculate_total()
        self.avg = self.total / 3
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total(self):
        return self.eng + self.c + self.py

    def calculate_grade(self):
        avg = self.avg
        if avg >= 95:
            return "A+"
        elif avg >= 90:
            return "A0"
        elif avg >= 85:
            return "B+"
        elif avg >= 80:
            return "B0"
        elif avg >= 75:
            return "C+"
        elif avg >= 70:
            return "C0"
        elif avg >= 65:
            return "D+"
        elif avg >= 60:
            return "D0"
        else:
            return "F"

    def printAllStu(self):
        print(self.id, "\t", self.name, "\t", self.eng, "\t", self.c, "\t", self.py,
                "\t", self.total, "\t", round(self.avg, 1), "\t", self.grade, "\t", self.rank)

class ManyStudent:
    def __init__(self):
        self.students = []

    def input_value(self, idx):
        id = input(f"{idx + 1}번째 학생의 학번을 입력하시오: ")
        name = input(f"{idx + 1}번째 학생의 이름을 입력하시오: ")
        eng = int(input(f"{idx + 1}번째 학생의 영어 점수를 입력하시오: "))
        c = int(input(f"{idx + 1}번째 학생의 c언어 점수를 입력하시오: "))
        py = int(input(f"{idx + 1}번째 학생의 파이썬 점수를 입력하시오: "))
        return Student(id, name, eng, c, py)

    def calculate_ranks(self):
        for s in self.students:
            s.rank = 1
            for other in self.students:
                if s.total < other.total:
                    s.rank += 1

    def insert_to_db(self, student):
        try:
            sql = """
                INSERT INTO students (id, name, eng, c, py, total, avg, grade, `rank`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                student.id, student.name, student.eng, student.c, student.py,
                student.total, student.avg, student.grade, student.rank
            ))
            conn.commit()
        except Exception as e:
            print("DB 삽입 중 오류 발생:", e)

    def delete_from_db(self, student_id):
        try:
            sql = "DELETE FROM students WHERE id = %s"
            cursor.execute(sql, (student_id,))
            conn.commit()
        except Exception as e:
            print("DB 삭제 중 오류 발생:", e)

    def addStu(self):
        if len(self.students) >= STUDENTS:
            print("더 이상 학생을 추가할 수 없습니다")
            return
        student = self.input_value(len(self.students))
        self.students.append(student)
        self.calculate_ranks()
        self.insert_to_db(student)

    def deleteStu(self):
        if len(self.students) == 0:
            print("삭제할 학생이 없습니다")
            return
        deleteOne = int(input("몇번째 학생을 삭제하시겠습니까? "))
        if 1 <= deleteOne <= len(self.students):
            student = self.students[deleteOne - 1]
            self.delete_from_db(student.id)
            del self.students[deleteOne - 1]
            self.calculate_ranks()
        else:
            print("입력 오류")

    def searchStu(self):
        key = input("학생의 이름이나 학번을 입력하시오: ")
        exist = False
        for student in self.students:
            if student.id == key or student.name == key:
                exist = True
                print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                student.printAllStu()
                break
        if not exist:
            print("해당 학생을 찾을 수 없습니다")

    def sortStu(self):
        if len(self.students) == 0:
            print("정렬할 학생이 없습니다")
            return
        self.students.sort(key=lambda s: s.total, reverse=True)
        self.calculate_ranks()
        print("정렬 완료")

    def printAll(self):
        print("\t\t성적관리 프로그램")
        print("=" * 85)
        print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("=" * 85)
        for s in self.students:
            s.printAllStu()

    def overthe_80(self):
        count = sum(1 for s in self.students if s.avg >= 80)
        print(f"80점 이상은 총 {count}명입니다")

def main():
    manager = ManyStudent()

    print("<<학생 성적 관리 프로그램>>")
    print(f"최대 {STUDENTS}명의 학생들의 각 학번, 이름, 영어 점수, C-언어 점수, 파이썬 점수를 입력하시오")
    for i in range(STUDENTS):
        student = manager.input_value(i)
        manager.students.append(student)
        manager.insert_to_db(student)
        print("")

    manager.calculate_ranks()

    while True:
        print("1. 삽입, 2. 삭제, 3. 탐색, 4. 정렬(총점), 5. 80점이상 학생 출력, 6. 전체 내용 출력, 0. 종료")
        choice = int(input("메뉴를 선택하시오: "))

        if choice == 6:
            manager.printAll()
        elif choice == 1:
            manager.addStu()
        elif choice == 2:
            manager.deleteStu()
        elif choice == 3:
            manager.searchStu()
        elif choice == 4:
            manager.sortStu()
        elif choice == 5:
            manager.overthe_80()
        elif choice == 0:
            print("프로그램을 종료합니다.")

            
            cursor.execute("TRUNCATE TABLE students")
            conn.commit()

            break
        else:
            print("잘못된 입력입니다.")

main()
