# Assignment class inheritance
class Student:
        #declaring init method
    def __init__(self, firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
  
class Group_lead(Student):

    def __init__(self,firstname,lastname,std=[]):
        self.std=std
        super().__init__(firstname, lastname)
        # declaring method that add student to the list of student
    def add_student(self,std):
        self.std.append(std)
        
        print(f"I will like to add {self.std} to student's list")
         # declaring method that add student to the list of student
    def remove_student(self,std):
        self.std.remove(std)
        #print(self.std)
        print(f" {self.std} is the student left after removing some students")
          # declaring method to print full name of student
    def display(self):
        return '{} {} '. format(self.firstname,self.lastname)
    def email(self):
        self.mail=self.firstname+"."+self.lastname.lower()+"@stutern.com"
        print(f"Email address of the student:{self.mail}")
        #instance of student class
group1=Group_lead("Amina","Lawal")
group2=Group_lead("Mariam","Adeoti")
group3=Group_lead("Joseph","Aroms")


print('The name of the Group1 Leader is:',group1.display())
group1.email()
group1.add_student("Aliyu Ahmed")
group1.add_student("Bashar Uthman")
group1.remove_student("Aliyu Ahmed")
print("The name of the group2 Leader is:",group2.display())
group2.email()
group2.add_student("Kafayat Ibrahim")
group2.add_student("Temitope Bamidele")
group2.remove_student("Kafayat Ibrahim")
print("The name of the group2 Leader is:",group3.display())
group3.email()
group3.add_student("Adekunle Lawal")
group3.add_student("Bidemi Ayeni")
group3.remove_student("Bidemi Ayeni")



