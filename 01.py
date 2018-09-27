'''
定义一个学生类
'''
#定义类
class Student():
    pass
#定义对象
fyq = Student()

class Python_student():
    name = "nana"
    age = 18
    course = 'python'
    def doHomework(self):
        print("我在做作业")
        return None
yueyue = Python_student()
yueyue.doHomework()
print(yueyue.age)
yueyue.name = "hehe"
print(Python_student.name)
print(id(Python_student.name))

print(id(yueyue.name))