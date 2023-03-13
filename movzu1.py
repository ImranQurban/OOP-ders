

# 13.03.23
# Class yaradacagiq ve classlarda bezi methodlarla mueyyen funksiyalar teyin edeceyik. 
# Qeyd 1: Java biliyim yoxdu deye python-da yazdim kodu. 
# Qeyd 2: OOP strukturuna ele de beled deyilem, ona gore yazdigim kod ele de pesekar olmaya biler. 



# 13. Write a method that receives a 2 digits number. Print 'yes' if the units equals to the tens. 

class units_equal_tens():

    def check(self, num):
        units = num % 10
        tens = num // 10
        print("units :", units)
        print("tens :", tens)
        if units == tens:
            return("yes")
        else: 
            return("no")

check = units_equal_tens()

print(check.check(13)) #no
print(check.check(22)) #yes

# KODUN IZAHI: 
# 1 - Evvelce bir class yaratdiq. Yaratdigimiz class-i adlandirdiq. 
# 2 - Sonra class icinde bir method yaratdiq. 
# 3 - method bu sekilde isleyir: 
# 3.1 ededin tekliklerini tapib onu "units" deyisenine deyer olaraq menimsedirik. 
# 3.2 ededin onluqlarini tapib onu "tens" deyisenine deyer olaraq menimsedirik. 
# 3.3 besit bir if-else dovresi qururuq. eger teklikler onluqlara beraberdirse, "yes" cap edirik. 
# eks halda "no" cap edirik. 



# BU METHOD-DA BEZI DEYISIKLIKLER DE EDE BILERIK : 
    
class units_equal_tens2():

    def check(self, num):
        if (num >= 10 and num<100):
            units = num % 10
            tens = num // 10
            print("units :", units)
            print("tens :", tens)
            if units == tens:
                return("yes")
            else: 
                return("no")
        else: 
            return "Daxil edilen eded 2 reqemli deyil!"
    

check2 = units_equal_tens2()

print(check2.check(13)) #no
print(check2.check(4)) #Daxil edilen eded 2 reqemli deyil!

# burada methoda ikinci bir if-else elave etdim. 
# bu zaman ilk once ededin iki reqemli olub-olunmadigi yoxlanilir. 


