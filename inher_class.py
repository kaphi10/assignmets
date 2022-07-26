# using inheritance 
class Person:
    #declaring init method
    def __init__(self, name,id):
        self.name=name
        self.id=id
    # declaring method to print
    def display(self):
        # print(self.name)
        # print(self.id)
        return '{} {} '. format(self.name,self.id)
    
# child class
class Student(Person):
    def __init__(self, name,id,facaulty,department):
        self.faculty=facaulty
        self.department=department
    
        #calling __init__ of person class i.e parent class
        Person.__init__(self, name,id)
    def dis(self):
        return '{} {} '. format(self.faculty,self.department)
declare=Student('Abdullahi Umar',1002,'Science','Computer Science')
print(declare.display() + declare.dis())