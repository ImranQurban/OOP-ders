""" 
Write a program that accepts 10 numbers and 
prints the sum of all the numbers that are higher than 20. 
"""

# while ve if ile:
# IZAH:
# i deyiseni input olaraq alacagimiz ededlerin nomresini bildirir.
# sum 20-den boyuk olan ededlerin cemini saxlayacaq.
# while dovru: i<=10 sertini yoxlayacaq.
# sert dogru olduqca istifadeciden bir input alib deyer olaraq num-a menimsedecek.
# if serti num-un 20-den boyuk olub-olmadigini yoxlayacaq, eger boyukdurse, sum-la toplanacaq.
# sonra i bir vahid artacaq.
# bu proses i 10-dan boyuk olana qeder davam edecek.
# while serti artiq true olaraq donmedikden sonra umumi cem cap edilecek.
""" 
i = 1
sum = 0 
while i<=10:
    num = int(input("Enter the number {}: ".format(i)))
    
    if num>20:
        sum+=num
    
    i+=1
print(sum)
 """

# method ve class-la:
# IZAH:
# Nums adli bir class yaradiriq.
# Nums-in icindeki __init__ funksiyasinde num1-den num10-a qeder nomrelenmis deyisenler var,
# bu deyisenler istifadecinin parametr olaraq vereceyi deyisenleri saxlayacaq.
# nums deyiseni bir list-dir, num-lari bir list elementi olaraq goturub saxlayacaq.
# check_numbers method-u:
# bu method-un icindeki sum deyiseni nums-un 20-den boyuk olan elementlerini toplamagimiza yarayacaq.
# method-un icindeki for dovru biz nums-un elementleri arasinda gezmeye imkan verir.
# for-un icindeki if serti ile nums-un elementlerinin 20-den boyuk olub-olmadigini yoxlayacagiq.
# eger boyukdurse, sum-la toplanacaq.
# dovr bitdikden sonra sum cap olunacaq.


class Nums:
    def __init__(self, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
        self.__num4 = num4
        self.__num5 = num5
        self.__num6 = num6
        self.__num7 = num7
        self.__num8 = num8
        self.__num9 = num9
        self.__num10 = num10
        self.__nums = [num1, num2, num3, num4,
                       num5, num6, num7, num8, num9, num10]

    def check_numbers(self):
        sum = 0
        for i in self.__nums:
            if i > 20:
                sum += i
        print(sum)


nums1 = Nums(1, 23, 43, 56, 12, 14, 15, 24, 3, 2)

nums1.check_numbers()  # 146
