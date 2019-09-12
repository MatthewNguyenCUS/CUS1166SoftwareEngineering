from mymodules.models import Student
from mymodules.math_utils import average_grade
if __name__ == '__main__':

    s0 = Student("John",90)
    s1 = Student("Tom",80)
    s2 = Student("Andrew",85)
    s3 = Student("Matthew",91)
    s4 = Student("Smith",95)
    s5 = Student("Jessica",99)
    s6 = Student("Alex",100)
    s7 = Student("Michelle",93)
    s8 = Student("Katherine",89)
    s9 = Student("Nicky",87)
    students = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]


    for i in students:
        i.print_student_info()
    print("Average: "+str(average_grade(students)))
