
# Students adli bir class yaratdiq:
# __init__ funksiya ile onun atributlarini teyin etdik
# double under score ile deyisenleri gizletdik

class Students: 
    def __init__ (self, __num_of_boys, __num_of_girls, __students):
        self.__num_of_boys = __num_of_boys #sinifdeki oglanlarin sayi
        self.__num_of_girls = __num_of_girls #sinifdeki qizlarin sayi
        self.__num_of_students = __num_of_boys + __num_of_girls #sinifdeki umumi usaqlarin sayi
        self.__students = __students #usaqlarin siyahisi
        
    def info(self): #obyektin atributlarini cap eden function
        print("Number of Boys : ", self.__num_of_boys)
        print("Number of Girls : ", self.__num_of_girls)
        print("Number of Students : ", self.__num_of_students)
        print("Students : ", self.__students)
        

# Classin atributlarina bir defelik list daxil ede bilmedim deye ayrica list yaratdim her obyekt ucun.
students1_students = ["Imran", "Asim", "Nigar", "Aynur", "Qurban"]
students2_students = ["Ibrahim", "Rehim", "Nazli"]
students3_students = ["Cavid", "Cefer", "Efsane", "Gunay", "Kenan", "Gulay"]


#Class ucun 3 ayri obyekt yaratdim, deyisenlere deyer verdim
students1 = Students(3, 2, students1_students)
students2 = Students(2, 1, students2_students)
students3 = Students(3, 3, students3_students)



# her object ucun info() function-unu cagirdim. 
print(students1.info()) 
""" 
Number of Boys :  3
Number of Girls :  2
Number of Students :  5
Students :  ['Imran', 'Asim', 'Nigar', 'Aynur', 'Qurban']
"""


print(students2.info())  
"""  
Number of Boys :  2
Number of Girls :  1
Number of Students :  3
Students :  ['Ibrahim', 'Rehim', 'Nazli']
"""

print(students3.info())   
""" 
Number of Boys :  3
Number of Girls :  3
Number of Students :  6
Students :  ['Cavid', 'Cefer', 'Efsane', 'Gunay', 'Kenan', 'Gulay']
"""