stu = []

def gradeCalculate(avg):
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

def pointCalculate(index, eng, c, py):
    total = eng + c + py
    avg = total / 3
    grade = gradeCalculate(avg)
    stu[index].append(total)
    stu[index].append(avg)
    stu[index].append(grade)

def rankCalculate(index, stu):
    rank = 1
    for i in range(5):
        if i == index:
            continue
        if stu[index][5] < stu[i][5]:
            rank += 1
    stu[index].append(rank)

for i in range(5):
    id = input("학번: ")
    name = input("이름: ")
    eng = int(input("영어: "))
    c = int(input("C-언어: "))
    py = int(input("파이썬: "))
    print("")

    stu.append([id, name, eng, c, py])
    pointCalculate(i, eng, c, py)

for i in range(5):
    rankCalculate(i, stu)

print("\t\t성적관리 프로그램")
print("=" * 85)
print("학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
print("=" * 85)

for i in stu:
    print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4], "\t", i[5], "\t", round(i[6], 1), "\t", i[7], "\t", i[8])
