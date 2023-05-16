x = 1

try: 
    print(x/0)
except TypeError: #TypeError-la qarsilassaq, bu except blokundaki kod icra olunacaq
    print("TypeError\nCheck if the value of variable x is a numeric value")
except: #TypeError xaricinde bir error-la qarsilassaq, bu except blokundaki kod icra olunacaq
    print("Something went wrong, but it is not TypeError")
else: #Error-la qarsilasmasaq, bu kod icra olunacaq
    print("Nothing went wrong")
finally: #Error-la qarsilasib qarsilasmamagimizdan asili olmayara bu blok icra olunacaq
    print("Try - except is finished")

