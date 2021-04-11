
# 类 python所有的类在创建的时候如果没有继承那最终都会继承于Object
class Human():
    # __init__方法的第一个参数永远是self表示实例创建本身
    def __init__(self,name,sex,years):
        self.name = name
        self.sex = sex
        self.years = years

    def pritn_info(self):
        print("姓名：%s|性别：%s|年龄：%d" %(self.name,self.sex,self.years))
    # 多态
    def who(self):
        print("父类")

class Student(Human):
    def __init__(self,name,sex,years,score,class_):
        super().__init__(name,sex,years)
        self.score = score
        self.class_ =  class_

    def print_Student(self):
        self.pritn_info()
        print("班级：%s|分数：%d"%(self.class_,self.score))

    def who(self):
        print("学生子类")

class Teacher(Human):
    def __init__(self,name,sex,years,subject,time):
        super().__init__(name,sex,years)
        self.subject = subject
        self.time = time

    def pritn_Teacher(self):
        self.pritn_info()
        print("科目：%s|入职年分：%d")

    def who(self):
        print("教师子类")

h1 = Human("小郑","男",21)
h1.pritn_info()

s1 = Student("小明","男",21,99,"1班")
s1.pritn_info()
s1.print_Student()

t1 = Teacher("静静","女",22,"英语",2021)
t1.pritn_info()
t1.pritn_Teacher()

# 判断该类是谁的子类
print(type(h1))
print(type(s1))
print(type(t1))

print(isinstance(h1,Human))
print(isinstance(s1,Human))
print(isinstance(t1,Human))
# 教师类不是学生类的子类，不属于学生类
print(isinstance(t1,Student))

# with语句
class Testwith():
    def __enter__(self):
        print("run")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("exit")
        else:
            print("something error")
# 实现上下文自动管理
with Testwith() as obj:
    print('with运行')
    raise NameError("testNameError")