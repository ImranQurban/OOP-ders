# EXCEPTION IZAH:
# Istifadeciden input olaraq bir text alacagiq
# eger text-in icinde [0,1,2,3,4,5,6,7,8,9] elementleri varsa:
# "text-inizde qadagan olunmus simvollar askarlandi" yazisi cixacaq.

def check_prohibited_characters(text):
    # input olaraq alacagimiz metn-de qadagan olunmus simvollarin olub-olmadigini yoxlayacagimiz deyisen
    prohibited_characters = set('0123456789')
    # text-deki her hansi bir simvolun qadagan olunmus simvollara beraber olub-olmadigini yoxlayan sert
    if any(char in prohibited_characters for char in text):
        # eger qadagan olunmus simvollar varsa, ValueError qaldiracagiq ve bu mesajla qarsilasacagiq
        raise ValueError("Your text contains prohibited characters")
    return text


user_input = input("Enter your text: ") #istifadeciden text aliriq
try:
    result = check_prohibited_characters(user_input) #text-i funksiyaya parametr olaraq veririk
    print("Text:", result) 
except ValueError as e: #error-la qarsilasiriqsa, bu kod bloku ise dusecek.
    print(str(e))
