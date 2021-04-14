#define a class of students in IBI
class Student:
    def __init__(self,first,last,undergraduate_programme):
        self.first=first
        self.last=last
        self.undergraduate_programme=undergraduate_programme
    #get the full name
    def full_name(self):
        return '{} {}'.format(self.first,self.last)


student_1=Student('Keying','Zhu','BMS')
student_2=Student('Wenli','Jin','BMS')

print(student_1.full_name(),student_1.undergraduate_programme)
print(student_2.full_name(),student_2.undergraduate_programme)
#if you want to input other students'information
a=input('Please write the first name of the student here:')
b=input('Please write the last name of the student here:')
c=input('Please write the undergraduate programme of the student:')
e=Student(a,b,c)
print(e.full_name()+'  '+e.undergraduate_programme)

