# Декомпозиция - разделение логики кода по модулям

from calc import add, sub # точечный импорт
# from test import hello

# hello()
print(__name__)

add(4, 9)
# sub(12, 5)

# from calc import * #  * - импорт всего содержимого

# add(4, 9)
# sub(12, 5)

# from calc import add as sum
from folder.test import add as mult

# sum(3,3)
mult(3,3)

# import calc # Импорт модуля

# calc.add(4, 9)
# calc.sub(12, 5)

# Кастомные модули:
# lesson_1.py, calc.py, test.py


# Встроенные модули:
# random, time, math, datetime

# import random
# random.choice()
# random.randint(1,100)

# from random import randint
# randint(40,200)


# import time

# while True:
#     print("loading...")
#     time.sleep(2)

# Внешние модули:


from termcolor import cprint, colored

cprint("Hello World!", "green", "on_blue", attrs=["bold"] )
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)