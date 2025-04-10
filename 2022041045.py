##################

#프로그램명: 성적처리 프로그램

#작성자: 2022041045 서민석

#작성일: 2025. 04. 09

#프로그램 설명: 

###################


STUDENTS = 5


class Student:
    def __init__(self, id, name, eng , c, py):
        self.id = id
        self.name = name
        self.eng = eng
        self.c = c
        self. py = py
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
        print(self.id, "\t", self.name, "\t", self.eng, "\t", self.c, "\t", self.py, "\t", self.total, "\t", round(self.avg, 1), "\t", self.grade, "\t", self.rank)


class ManyStudent:
    def __init__(self):
        self.students = []

    def input_value(self, idx):
        id=input(f"{idx+1}번째 학생의 학번을 입력하시오: ")
        name=input(f"{idx+1}번째 학생의 이름을 입력하시오: ")
        eng=int(input(f"{idx+1}번째 학생의 영어 점수를 입력하시오: "))
        c=int(input(f"{idx+1}번째 학생의 c언어 점수를 입력하시오: "))
        py=int(input(f"{idx+1}번째 학생의 파이썬 점수를 입력하시오: "))
        return Student(id, name, eng, c, py)

    def calc1ulate_ranks(self):
        for s in self.students:
            s.rank = 1
            for other in self.students:
                if s.total < other.total:
                    s.rank += 1

    
    def addStu(self):
        if len(self.students)>=STUDENTS:
            print("더 이상 학생을 추가할 수 없습니다")
            return
        else: 
            self.students.append(self.input_value(len(self.students)))
            self.calculate_ranks()

                
    def deleteStu(self):
        if len(self.students) ==0:
            print("삭제할 학생이 없습니다")
            return
        else:
            deleteOne=int(input("몇번째 학생을 삭제하시겠습니까?"))

            if 1<=deleteOne <=len(self.students):
                del self.students[deleteOne -1]
                self.calculate_ranks()
            else: 
                print("입력 오류")

    def searchStu(self):
        key = input("학생의 이름이나 학번을 입력하시오: ")
        exist = 0

        for student in self.students:
            if student.id == key or student.name == key:
                exist = 1
                print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print(student.id, "\t", student.name, "\t", student.eng, "\t", student.c, "\t", student.py, "\t", student.total, "\t", round(student.avg, 1), "\t", student.grade, "\t", student.rank)
                break

        if exist ==0:
            print("해당 학생을 찾을 수 없습니다")
            return 
        

    def sortStu(self):
        stuLen = len(self.students)
        if stuLen == 0:
            print("정렬한 학생이 업습니다")

        for i in range(stuLen):
            maxIdx = 1
            for j in range(i +1, stuLen):
                if self.students[j].total > self.students[maxIdx].total:
                    maxIdx = j

            if maxIdx != i:
                self.students[i], self.students[maxIdx] = self.students[maxIdx], self.students[i]

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
        count = 0
        for i in self.students:
            if i.avg >= 80:
                count +=1
        print(f"80점 이상은 총 {count}명입니다")
        


def main():
    manager = ManyStudent()
    print("<<학생 성적 관리 프로그램>>")
    print(f"최대 {STUDENTS}명의 학생들의 각 학번, 이름, 영어 점수, C-언어 점수, 파이썬 점수를 입력하시오")
    for i in range(STUDENTS):
        manager.students.append(manager.input_value(i))
        print("")

    manager.calculate_ranks()
    
    while True:
        print("1. 삽입, 2. 삭제, 3. 탐색, 4. 정렬(총점), 5. 80점이상 학생 출력, 6. 전체 내용 출력, 0. 종료")
        choice=int(input("메뉴를 선택하시오: "))

        if choice==6:
            manager.printAll()
        elif choice==1:
            manager.addStu()
        elif choice==2:
            manager.deleteStu()
        elif choice==3:
            manager.searchStu()
        elif choice==4:
            manager.sortStu()
        elif choice==5:
            manager.overthe_80()
        else:
            break


main()