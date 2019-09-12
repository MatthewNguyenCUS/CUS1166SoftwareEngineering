class Student():
    def __init__(self,student_name="",student_grade=0):
        self.student_name = student_name
        self.student_grade = student_grade

    def setGrade(self,student_grade):
        self.student_grade = student_grade

    def getGrade(self):
        return self.student_grade

    def print_student_info(self):
        print("Name: "+self.student_name+"\n"+"Grade: "+str(self.student_grade)+"\n")

#s = Student("John")
#s.setGrade(95)
#s.print_student_info()
