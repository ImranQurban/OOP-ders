class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        
    def person(self):
        print("ID:", self.id)
        print("Name:",self.name)
        print("Age:",self.age)
        
    def greetings():
        print("Hello, have a good day!")
        

class teacher(Person):
    def __init__(self, id, name, age, profession, experience, graduating_year):
        super().__init__(id, name, age)
        self.profession = profession
        self.experience = experience
        self.graduating_year = graduating_year
    
    def additonal_info(self):
        print("Experience:",self.experience)
        print("Graduating year:",self.graduating_year)
        print("Profession:",self.profession)
        
    def teachs(self):
        print(f"I teach {self.profession} in the university ")
        
    
class student(Person):
    def __init__(self, id, name, age, GPA, group_number, enterance_year):
        super().__init__(id, name, age)
        self.GPA = GPA
        self.group_number = group_number
        self.enterance_year = enterance_year
        
    def additonal_info(self):
        print("GPA:",self.GPA)
        print("Group number:",self.group_number)
        print("Enterance year:",self.enterance_year)
        
    def pass_exam(self):
        result =True
        if self.GPA > 5.0:
            print(result)
        else:
            print(not result)
            

teacher1 = teacher(1, 'kenan', 'quliyev', 'math', 5, '1998')
student1 = student(1, 'imran', 'qurbanzade', 5.1, '691.20', '2020')

teacher1.person()
teacher1.teachs()
teacher1.additonal_info()
teacher.greetings()

student1.pass_exam()
student1.person()
student1.additonal_info()
student.greetings()
            
    
            
            
        