""" 
13.  Create 3 objects of encapsulated Subject class that has following properties and methods
-  id
-  name
-  lectureHour
-  labHour
-  seminar
-  courseWork(Boolean)
+ info(){};
-  prints info about subject
"""

# __init__ funksiyasi python-daki class atributlarini teyin etmek ucun istifade olunur.
# self acar sozu ise hemin atributlara xaricden muraciet edile bilinsin istifade olunur.
# qeyd edim ki, python-da java-daki "private" acar sozu yoxdur.
# onun yerine double under score (__) istifade olunur.
# men de burda double under score-dan istifade edib deyisenleri gizli elan etmisem.


class Subject:
    def __init__(self, ID, name, LectureHour, LabHour, SeminarHour, CourseWork):
        self.__ID = ID
        self.__name = name
        self.__LectureHour = LectureHour
        self.__LabHour = LabHour
        self.__SeminarHour = SeminarHour
        self.__CourseWork = CourseWork

        # funksiyanin izahi:
        # fenn melumatlarini bir-bir ortaya cixaracaq.
    def info(self):
        print("Subject ID: ", self.__ID)
        print("Subject Name: ", self.__name)
        print("Lecture Hour: ", self.__LectureHour)
        print("Lab Hour: ", self.__LabHour)
        print("Seminar: ", self.__SeminarHour)
        print("Course Work: ", self.__CourseWork)


subject1 = Subject(1, "OOP", 30, 30, 15, False)
subject2 = Subject(2, "Web Programming", 30, 30, 15, True)
subject3 = Subject(3, "Data Analysis", 30, 30, 15, False)


print("subject1 data:")
subject1.info()
""" 
Subject ID:  1
Subject Name:  OOP
Lecture Hour:  30
Lab Hour:  30
Seminar:  15
Course Work:  False
"""
print("---------")
print("subject2 data:")
subject2.info()
""" 
Subject ID:  2
Subject Name:  Web Programming
Lecture Hour:  30
Lab Hour:  30
Seminar:  15
Course Work:  True
"""
print("---------")
print("subject3 data:")
subject3.info()
""" 
Subject ID:  3
Subject Name:  Data Analysis
Lecture Hour:  30
Lab Hour:  30
Seminar:  15
Course Work:  False
"""


#subject1.__id = 4
# burda gorunduyu kimi 'subject1' adli obyektin id-sini deyisirik, amma capa verdikde wmumi netice deyismir
# subject1.info()


# Gizli atributlarin nece islediyini gostermek ucun ikinci bir numune yaradaq:


"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        
        
person1 = Person("Imran", 19)
print(person1.info())
# Name :  Imran
# Age :  19

person1.age = 25
print(person1.info()) 

"""
#Name :  Imran
#Age :  25


# Subject class-inda gizli deyisenlere yeni bir deyer teyin etsek bele,
# info() funksiyasini cagirdiqda hec bir deyisiklik bas vermirdi.

# Person class-inda gorduyumuz kimi age deyisenine yeni bir deyer teyin etdik
# ve info() funksiyasini cagirdiqda deyer deyisdi.
