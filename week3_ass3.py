# Assignment class inheritance
class Student:
        #declaring init method
    def __init__(self, firstname,lastname,):
        self.firstname=firstname
        self.lastname=lastname
    # declaring method to print
    def display(self):
        # print(self.name)
        # print(self.id)
        return '{} {} '. format(self.firstname,self.lastname)

class Group_lead(Student):
    std=[]
    other=[]
    def __init__(self,firstname,lastname,std):
        super().__init__(firstname, lastname)
        
        self.std=std
        
        
    def add_student(self):
        self.other=self.std.append(self.other)
        return self.other
        
    
group1=Group_lead(firstname='Amina',lastname='Abubakar',std=['Aliyu Abdullahi','Kafayat Ibrahim'])
print('The name of the Group1 Leader is:',group1.display() + 
'The name of the student assigned to the group is',group1.std)
print('I will like to add mor student to group1:',group1.add_student(list('aisha aina')))