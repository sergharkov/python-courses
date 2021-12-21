class Validate:
    def __init__(self, Val):
        self.Val = Val       
    def Vstr(self):
        try:
            if (type(self.Val) is not str):
                raise TypeError
            return self.Val.lower()
        except  TypeError:
             print (f"Class is working with strings only")
             raise       
    def Vint(self):
        try:
            if (type(self.Val) is not int):
                raise TypeError
            return int(self.Val)
        except  TypeError:
             print (f"Class is working with strings only")
             raise
class Person:
    def __init__(self, first_name = 'N/A', last_name = 'N/A', birth_date = 'N/A'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
    
    def set_first_name(self,set_first_name):
        self.first_name = Validate(set_first_name).Vstr()
    
    def set_last_name(self,set_last_name):
        self.last_name = Validate(set_last_name).Vstr()
    
    def set_birth_date(self,set_birth_date):
        self.birth_date = Validate(set_birth_date).Vstr()
#v2   validate        
    def check_type(self,ch_str):
        if isinstance(ch_str, str):
            return ch_str.lower()
        else:
            raise TypeError("Class is working with strings only")
    
class Student(Person):
    def __init__(self):
        super(Student,self).__init__()
        self.course = 'N/A'
        self.university = 'N/A'
        
    def set_course(self,set_course):
        self.course = self.check_type(set_course)
#       self.course = Validate(set_course).Vstr()
        
    def set_university(self,set_university):
        self.university = Validate(set_university).Vstr()     
    
class Teacher(Person):
    def __init__(self):
        super(Teacher,self).__init__()
        self.salary = 'N/A'
        self.university = 'N/A'
        self.course = 'N/A'
        
    def set_course(self,set_course):
        self.course = Validate(set_course).Vint()
        
    def set_university(self,set_university):
        self.university = Validate(set_university).Vstr()  
    
    def set_salary(self,set_salary):
        self.salary = Validate(set_salary).Vstr()
        


s1,t1,p = Student(),Teacher(),Person()

print("Person ",p.first_name,p.last_name,p.birth_date)
print("Student ",s1.first_name,s1.last_name,s1.birth_date,s1.course,s1.university)
print("Teacher ",t1.first_name,t1.last_name,t1.birth_date,t1.salary)


p.set_first_name('Serg')
p.set_last_name('Kharkov')
p.set_birth_date('22041986')


s1.set_first_name('stud_Serg')
s1.set_last_name('stud_Kharkov')
s1.set_birth_date('22041986')
s1.set_university('stud_KPI')
s1.set_course('22041986')

t1.set_first_name('teacher_Serg')
t1.set_last_name('teacher_Kharkov')
t1.set_birth_date('22041986')
t1.set_salary('22041986')

#p.set_university('KPI')
print("----------------------")
print("Person ",p.first_name,p.last_name,p.birth_date)
print("Student ",s1.first_name,s1.last_name,s1.birth_date,s1.course,s1.university)
print("Teacher ",t1.first_name,t1.last_name,t1.birth_date,t1.salary)
