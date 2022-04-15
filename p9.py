           class Student:
    rollNumber = None
    name = None

class Exam(Student):
    marks = []


class Result(Exam):
    def print_total(self):
        print(sum(self.marks))



r = Result()


r.name = (input("Enter name of student : "))
r.rollNumber = int(input("Enter roll number of student : "))

for i in range(1,7):
    r.marks.append(int(input("Enter marks of "+str(i) + " subject : ")))

print("Total marks : ")
r.print_total()
