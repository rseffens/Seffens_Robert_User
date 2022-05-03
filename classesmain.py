
class Stack:
    def __init__(self, name, grade ):
        self.name = name
        self.grade = grade

    def info(self): 
        print("Name : ", self.name)
        print("grad: ", self.grade)

class Student: 
    #class atribute placed between class and first def#
    student_list = [] #each time a sutdent is added, a reference will be added

    #adding a stack attribute - association
    def __init__( self, first_name, last_name, id, stack ):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.stack = stack
        Student.student_list.append ( self )
        

    def student_info( self ):
        print( "First name: ", self.first_name )
        print( "Last name: ", self.last_name )
        print( "Id : ", self.id)
        self.stack.info()
        return self

    def change_full_name( self, f_name, l_name ):
        self.first_name = f_name
        self.last_name = l_name
        return self

    def get_full_name(self):
        return self.first_name + " " + self.last_name


    def updateGrade( self, grade):
        self.stack.grade = grade
        return self

#Class Method (looking through array to grave information)
    @classmethod
    def print_all_students( cls ):
        for student in cls.student_list:
            student.student_info

#static method
    def add_two_numbers( num1, num2):
        return num1 + num2 

class Math:
    def add_two_numbers(num1,num2):
        return num1+num2
    
    def subtract_two_numbers(num1,num2):
        return num1-num2

    def multiply_two_numbers(num1,num2):
        return num1*num2

    def divide_two_numbers(num1,num2):
        return num1/num2
    
    def power(num, exponential):
        result = 1.0

        for x in range( 0, exponential ):
                result*=num
                return result