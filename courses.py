class Student:
    #def __init__(self, student_id, course_id, marks, age, fees):
    def __init__(self):
        self.__student_id = None
        self.__course_id = None
        self.__marks = None
        self.__age = None
        self.__fees = None
        
    def set_student_id(self, student_id):
            self.__student_id = student_id
        
    def get_student_id(self):
            return self.__student_id
        
        
        
        
    def get_course_id(self):
        return self.__course_id
        
    def set_marks(self, marks):
        self.__marks = marks
        
    def get_marks(self):
        return self.__marks
        
    def set_fees(self, fees):
        self.__fees = fees
        
    def get_fees(self):
        return self.__fees
        
    def set_age(self, age):
        self.__age = age
        
    def get_age(self):
        return self.__age
        
    def set_student_id(self, student_id):
        self.__student_id = student_id
        
    def get_student_id(self):
        return self.__student_id
            
    def validate_marks(self):
        if self.__marks >= 0 and self.__marks < 100:
            return True
        else:
            return False
        
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False
        
    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False
        
        
    def check_course(self, course_id):
        if course_id not in ('1001','1002'):
            return False
        if course_id == '1001' and self.__marks > 85:
            self.__course_id = course_id
            self.set_fees(25575 - (25575 * .25))
            return True
        else:
            self.__course_id = course_id
            self.set_fees(25575 - (25575 * .25))
            return True
            
        if course_id == '1002' and self.__marks > 85:
            self.__course_id = course_id
            self.set_fees(15500 - (15500 * .25))
            return True
        else:
            self.__course_id = course_id
            self.set_fees(15500 - (15500 * .25))
            return True
            

s1 = Student()    
s1.set_age(25)
s1.set_marks(65)
print(s1.check_course('1001'))
print(s1.get_fees())
print(s1.check_qualification())
        
        
        
        
        
