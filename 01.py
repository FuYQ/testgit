'''
定义一个学生类
'''
#定义类
class Student():
    pass
#定义对象
fyq = Student()

class Python_student():
    name = None
    age = 0
    course = 'python'
    def doHomework(self):
        print("我在做作业")
        return None
yueyue = Python_student()
yueyue.doHomework()
print(yueyue.age)
print(yueyue.__dict__)