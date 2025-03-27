
STUDENTS = 1
stu=[]

def main():
    print("<<학생 성적 관리 프로그램>>")
    print(f"최대 {STUDENTS}명의 학생들의 각 학번, 이름, 영어 점수, C-언어 점수, 파이썬 점수를 입력하시오")
    for i in range(STUDENTS):
        stu.append(input_value(i))
        print("")

    calculate_ranks()
    
    while True:
        print("1. 삽입, 2. 삭제, 3. 탐색, 4. 정렬(총점), 5. 80점이상 학생 출력, 6. 전체 내용 출력, 0. 종종료")
        choice=int(input("메뉴를 선택하시오: "))

        if choice==6:
            printAll()
        elif choice==1:
            addStu(stu)
        elif choice==2:
            deleteStu(stu)
        elif choice==3:
            searchStu(stu)
        elif choice==4:
            sortStu(stu)
        elif choice==5:
            overthe_80(stu)
        else:
            break
        


def input_value(i):
    id=input(f"{i+1}번째 학생의 학번을 입력하시오: ")
    name=input(f"{i+1}번째 학생의 이름을 입력하시오: ")
    eng=int(input(f"{i+1}번째 학생의 영어 점수를 입력하시오: "))
    c=int(input(f"{i+1}번째 학생의 c언어 점수를 입력하시오: "))
    py=int(input(f"{i+1}번째 학생의 파이썬 점수를 입력하시오: "))


    student=[id, name, eng, c, py]
    total, avg = calculator(student)
    student.extend([total, avg])
    student.append(grade(avg))
    return student


def calculator(student):
    total=sum(student[2:5])
    avg= total/3

    calculedList=[total, avg]
    return calculedList


def grade(avg):
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



def calculate_ranks():
    for i in range(len(stu)):
        rank = 1
        for j in range(len(stu)):
            if i != j and stu[i][5] < stu[j][5]:  
                rank += 1
        stu[i].append(rank)


def printAll():
    print("\t\t성적관리 프로그램")
    print("=" * 85)
    print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("=" * 85)

    for i in stu:
        print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", round(i[6], 1), "\t", i[7], "\t", i[8])

def addStu(stu):
    if len(stu)>=STUDENTS:
        print("더 이상 학생을 추가할 수 없습니다")
        return
    else: 
        stu.append(input_value(len(stu)))
        calculate_ranks()

def deleteStu(stu):
    if len(stu)==0:
        print("삭제할 학생이 없습니다")
        return
    else:
        deleteOne=int(input("몇번째 학생을 삭제하시겠습니끼?"))
        
        if 1<= deleteOne<=len(stu):
            del stu[deleteOne-1]
            calculate_ranks()
        else: print("입력 오류")

def searchStu(stu):
    key = input("학생의 이름이나 학번을 입력하시오: ")
    exist =0

    for student in stu:
        if student[0] == key or student[1] == key:
            exist=1
            print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
            print(student[0], "\t", student[1], "\t", student[2], "\t", student[3], "\t", student[4], "\t", student[5], "\t", round(student[6], 1), "\t", student[7], "\t", student[8])
            break

    if exist==0:
        print("해당 학생을 찾을 수 없습니다")
        return
    

def sortStu(stu):
    stuLen=len(stu)
    if stuLen==0:
        print("정렬할 학생이 없습니다")
    

    for i in range(stuLen):
        maxIdx=i
        for j in range(i+1, stuLen):
            if stu[j][5] > stu[maxIdx][5]:
                maxIdx=j
        if maxIdx != i:
            stu[i], stu[maxIdx] = stu[maxIdx], stu[i]

    calculate_ranks()
    print("정렬 완료")


def overthe_80(stu):
    count=0
    for i in stu:
        if i[6] >=80:
            count+=1

    
    print(f"80점 이상은 총 {count}명입니다")


main()

    






