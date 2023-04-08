""" 
13. Write a program that accepts 10 numbers in array. Print the even elements' sum. 
"""

# IZAH:
# Nums class-indaki __init__ funksiyasinda:
# num1-den num10-a qeder siralanmis deyisenler var.
# bu deyisenler obyektin parametrlerini ozunde saxlayacaq.
# nums listi num-lari element olaraq goturecek.
# sum_pf_even_numbers method-undaki for-la biz bir-bir nums list-indeki elementleri yoxlayacagiq.
# cut olanlari 0 deyeri verdiyimzi sum-la toplayacagiq.
# for dovru bitdikden sonra da sum-i cap edeceyik.


class Nums:
    def __init__(self, __num1, __num2, __num3, __num4, __num5, __num6, __num7, __num8, __num9, __num10):
        self.__num1 = __num1
        self.__num2 = __num2
        self.__num3 = __num3
        self.__num4 = __num4
        self.__num5 = __num5
        self.__num6 = __num6
        self.__num7 = __num7
        self.__num8 = __num8
        self.__num9 = __num9
        self.__num10 = __num10
        self.__nums = [__num1, __num2, __num3, __num4,
                       __num5, __num6, __num7, __num8, __num9, __num10]

    def sum_of_even_numbers(self):
        sum = 0
        for i in self.__nums:
            if i % 2 == 0:
                sum += i

        print("The sum of the even numbers:", sum)


nums1 = Nums(12, 34, 23, 45, 64, 76, 87, 98, 124, 142)

nums1.sum_of_even_numbers()
