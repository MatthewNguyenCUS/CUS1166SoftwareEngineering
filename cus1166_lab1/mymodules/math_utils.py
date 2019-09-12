def average_grade(roster):
    sum = 0
    students = 0
    for i in roster:
        students+=1
        sum += i.getGrade()
    return sum/students
