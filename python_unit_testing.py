import unittest

# unittest - python-da yazilan kodlari test etmek ucun istifade olunan bir moduldur.

# asagidaki numunede iki arqument alan ve onlari toplayib qaytara "add" funksiyasini test edirik.


def add(a, b):
    return a + b


# bu class unittest-in testing-ini icra etmeye komek eden bir class-dir
class TestAddFunction(unittest.TestCase):

    # testing prosesini bildirmek ucun her bir method-un adini "test_" prefiksi baslayiriq.
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-5, -7)
        self.assertEqual(result, -12)

    def test_add_zero(self):
        result = add(10, 0)
        self.assertEqual(result, 10)

    """ def test_add_non_numeric_values(self):
        result = add(0, "Imran")
        self.assertEqual(result, 0+"Imran") """


if __name__ == '__main__':  # basqa bir modul import etdiyimizde bu serti yaziriq ki, proqram duzgun islesin
    unittest.main()


# ilk 3 method olduqda hec bir error cixmayacaq.
# cunki daxil edilen her iki arqument ededi deyerlerdir.
# 4-cu method (test_add_non_numeric_values) bir ededi deyer,
# ve bir qeyri-ededi daxil etdikde ise error aliriq.


#ilk 3 method movcud olduqda output:

#Ran 3 tests in 0.001s

#OK


# 4 method da isledikde output:
#Ran 4 tests in 0.002s

#FAILED (errors=1)
