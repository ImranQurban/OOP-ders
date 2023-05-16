def greeting():  # Musteri magazaya girende isci onu salamlayir
    print("Hello\nWelcome to our store!")


class book_purchase():
    def __init__(self):
        self.books = ["1984",  "taun", "fahrenheit 451", "maymunlar gezegeni", "martin eden",
                      "sirin portagal agacim", "atama mektub", "cevrilme", "eli ve nino"]  # Magazada olan kitablar

        self.prices = {
            self.books[0]: 5.20,
            self.books[1]: 6.90,
            self.books[2]: 11.10,
            self.books[3]: 8.70,
            self.books[4]: 12.50,
            self.books[5]: 5.60,
            self.books[6]: 3.90,
            self.books[7]: 4.20,
            self.books[8]: 7.50
        }  # Magazada olan kitablarin qiymetleri

    def purchase(self):
        # User-den hansi kitabi istediyini sorusuruq
        wanted_book = input("Which book do you want? ")
        found = False  # kitab magazada varsa, True-ya cevrilecek boolean
        for book in self.books:  # kitab-in olub-olmadigini yoxlamaq ucun for dovresi aciriq
            if wanted_book.upper() == book.upper():  # if-le bu serti yoxlayiriq
                found = True  # kitab movcuddursa, True-ya ceviririk
                print(f"The price of {book} is {self.prices[book]}")
                # istifadeciden kitabi almaq isteyib-istemediyini sorusuruq
                purchase_request = input("Do you want to buy the book? ")
                if purchase_request.upper() == "yes".upper():
                    # kitabi alarken odenisi nece etidiyini sorusuruq
                    payment_method = input("Will you pay in cash or by card? ")
                    if payment_method.upper() == "card".upper():  # odenis kartla olacaq
                        print("Please bring the card close to the pos-terminal")
                        print("Thanks!")
                    elif payment_method.upper() == "cash".upper():  # odenis nagdla olacaq
                        # input string olaraq alinir deye biz onu floata ceviririk
                        money_paid = float(
                            input((f"The price is {self.prices[book]}: ")))
                        if money_paid > self.prices[book]: 
                            print("Here is your change: ",
                                  money_paid-self.prices[book]) #nagd pul qiymetden coxdursa, qaligi qaytaririq
                        elif money_paid < self.prices[book]:
                            print("You have to pay more",
                                  self.prices[book]-money_paid) #nagd pul qiymetden azdirsa, musteriye deyirik
                        else:
                            print("Thanks!")
                        break
                elif purchase_request.upper() == "no".upper(): #istifadeci kitabi almaq istemir
                    print("Ok")
                    break
        if not found: #found false-dursa, kitab yoxdur ve bunu bildiririk
            print("I'm sorry\nWe don't have this book")


print("------------------")
greeting()

purchase1 = book_purchase()

purchase1.purchase()
