#create a class firstly
class Student_grade:
    def __init__(self,name,code,poster,exam):
        self.name=name
        self.code=code
        self.poster=poster
        self.exam=exam
    #get the final grade
    def final_grade(self):
        return (int(self.code*0.4+self.poster*0.3+self.exam*0.3))
#here is the example   
student=Student_grade('Zhang San',86,98,91)

print(student.name,student.final_grade())

#input other students' information
a=input('Please write name of the student here:')
b=int(input('Please write the grade for code :'))
c=int(input('Please write the grade for poster:'))
d=int(input('Please write the grade for exam:'))
e=Student_grade(a,b,c,d)
print(a+'  '+str(e.final_grade()))
